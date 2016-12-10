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
    SECRET_KEY='Undivine41295812981'
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


# PUBLIC PAGES
@app.route('/')
def home():
    db = get_db()
    cur = db.cursor()
    cur.execute('select id, name, bosses, normal, heroic, mythic, show from progression order by id asc;')
    raids = cur.fetchall()
    cur.execute('select id, class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio from recruitment order by id asc;')
    recruitment = cur.fetchall()
    return render_template('index.html', raids=raids, recruitment=recruitment)


@app.route('/apply')
def apply():
    return render_template('apply.html')


# PUBLIC FUNCTIONS
@app.route('/add_app', methods=['POST'])
def add_app():
    db = get_db()
    cur = db.cursor()
    cur.execute('insert into applications (name, age, country, battletag, armory, specs, rig, experience, improve, what_it_takes, ui, logs, headset, raids, prevention, additional) '
                'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (request.form['name'], request.form['age'], request.form['country'], request.form['battletag'], request.form['armory'], request.form['specs'], request.form['rig'],
                 request.form['experience'], request.form['improve'], request.form['what_it_takes'], request.form['ui'], request.form['logs'], request.form['headset'], request.form['raids'],
                 request.form['prevention'], request.form['additional']))
    db.commit()
    flash('Application submitted')
    return redirect(url_for('home', _external=True, _scheme='http'))


# ADMIN PAGES
@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    return render_template('admin.html')


@app.route('/raids')
def raids():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('select id, name, bosses, normal, heroic, mythic, show from progression order by id asc;')
    raids = cur.fetchall()
    return render_template('admin_raids.html', raids=raids)


@app.route('/apps')
def apps():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('select id, name, age, country, battletag, armory, specs, rig, experience, improve, what_it_takes, ui, logs, headset, raids, prevention, additional, datetime '
                'from applications order by id desc')
    apps = cur.fetchall()
    return render_template('admin_apps.html', apps=apps)


@app.route('/recruitment')
def recruitment():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('select id, class, spec1, spec1_prio, spec2, spec2_prio, spec3, spec3_prio, spec4, spec4_prio from recruitment order by id asc;')
    recruitment = cur.fetchall()
    return render_template('admin_recruitment.html', recruitment=recruitment)


# ADMIN FUNCTIONS
@app.route('/add_raid', methods=['POST'])
def add_raid():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('insert into progression (name, bosses, normal, heroic, mythic, show) values (%s, %s, %s, %s, %s, %s)',
                (request.form['raid'], request.form['bosses'], request.form['normal'], request.form['heroic'], request.form['mythic'], 'Show'))
    db.commit()
    return redirect(url_for('raids', _external=True, _scheme='http'))


@app.route('/edit_raid', methods=['POST'])
def edit_raid():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('update progression set name=%s, bosses=%s, normal=%s, heroic=%s, mythic=%s, show=%s where id=%s',
                (request.form['raid'], request.form['bosses'], request.form['normal'], request.form['heroic'], request.form['mythic'], request.form['show'], request.form['id']))
    db.commit()
    return redirect(url_for('raids', _external=True, _scheme='http'))


@app.route('/edit_recruitment', methods=['POST'])
def edit_recruitment():
    if not session.get('logged_in'):
        return redirect(url_for('login', _external=True, _scheme='http'))
    db = get_db()
    cur = db.cursor()
    cur.execute('update recruitment set spec1_prio=%s, spec2_prio=%s, spec3_prio=%s, spec4_prio=%s where id=%s',
                (request.form['spec1'], request.form['spec2'], request.form['spec3'], request.form['spec4'], request.form['id']))
    db.commit()
    return redirect(url_for('recruitment', _external=True, _scheme='http'))


# USER ACCOUNTS
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        cur = db.cursor()
        cur.execute('select * from users where name = %s', (request.form['username'], ))
        user = cur.fetchone()
        if not user:
            error = 'Invalid username or password'
        elif not check_password_hash(user[2], request.form['password']):
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            return redirect(url_for('admin', _external=True, _scheme='http'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home', _external=True, _scheme='http'))


if __name__ == "__main__":
    # ONLY COMMENT IN IF YOU WANT TO REBUILD THE ENTIRE DATABASE!! (THIS ERASES ALL DATA) REDO SCHEMA.SQL BEFORE USING
    #init_db()
    #app.run()  # local
    app.run(host='0.0.0.0', port=int(os.environ['PORT'])) #web
