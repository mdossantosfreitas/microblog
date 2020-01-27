from flask import render_template
from app import app

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