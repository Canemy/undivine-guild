import os
import sqlite3
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# create our little application :)
from flask import json

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'guild.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with closing(sqlite3.connect(app.config["DATABASE"])) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            print("executing schema.sql")
            db.cursor().executescript(f.read())
            db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

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
    return redirect(url_for('home'))

@app.route('/apps')
def show_entries():
    db = get_db()
    cur = db.execute('select id, battletag, experience, class, improve, attendance, rig, personal, checked, datetime from applications order by id desc')
    apps = cur.fetchall()
    return render_template('apps.html', apps=apps)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

if __name__ == "__main__":
    if not os.path.isfile("guild.db"):
        init_db()
    app.run()