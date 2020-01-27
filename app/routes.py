from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import  LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = { 'username' : 'Miguel'}
    posts =  [
        {
            'author' : {'username' : 'Matheus dos Santos Freitas'},
            'body' : 'Hello Guys, first post'
        },
        {
            'author' : {'username' : 'Raul Borges'},
            'body' : 'Parasite best movie'
        }
    ]
    return render_template('index.html', title='Home', user = user, posts = posts)

@app.route("/login", methods=['GET', 'POST']) ##it will run for get and post
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data)) ##flash from flask
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form = form)