import os
import psycopg2
import urllib.parse as urlparse
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# create our little application :)
from flask import json
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'guild.db'),
    SECRET_KEY  ='ImperfectionGuildSite'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def connect_db():
    """Connects to the specific database."""
    rv = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    return rv

def init_db():
    with closing(psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            print("executing schema.sql")
            db.cursor().execute(f.read())
            db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'psql_db'):
        g.psql_db = connect_db()
    return g.psql_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'psql_db'):
        g.psql_db.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into applications (battletag, experience, class, improve, attendance, rig, personal) values (?, ?, ?, ?, ?, ?, ?)',
               [request.form['battletag'], request.form['experience'], request.form['class'], request.form['improve'], request.form['attendance'], request.form['rig'], request.form['personal']])
    db.commit()
    flash('Application submitted')
    return redirect(url_for('home', _external=True, _scheme='http'))


@app.route('/apps')
def apps():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.execute('select id, battletag, experience, class, improve, attendance, rig, personal, checked, datetime from applications order by id desc')
    apps = cur.fetchall()
    return render_template('apps.html', apps=apps)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        cur = db.execute('select * from users where name = ?', [request.form['username']])
        user = cur.fetchone()
        if not user:
            error = 'Invalid username'
        elif not check_password_hash(user["pw_hash"], request.form['password']):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('apps', _external=True, _scheme='http'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('apps', _external=True, _scheme='http'))


if __name__ == "__main__":
    if not os.path.isfile("guild.db"):
        init_db()
    app.run() #local
    #app.run(host='0.0.0.0', port=int(os.environ['PORT'])) #web
