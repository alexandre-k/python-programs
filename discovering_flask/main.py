from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   session,
                   flash)
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.secret_key = 'fv9023cw3fID02'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from models import *

def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def home():
    posts = (entry for entry in db.session.query(BlogPost).all())
    posts_dict_format = { post.title: post.description for post in posts }
    return render_template('welcome.html', posts=posts_dict_format)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'geQoe120ck':
            error = 'Invalid credentials.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('welcome')) # to home function
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You wre just logged out in!')
    return redirect(url_for('welcome'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 80, debug=True)

