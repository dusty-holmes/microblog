from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dusty'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
       'index.html', 
       title="Home",
       user=user,
       posts=posts
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    app.logger.info(f'Submit with method {request.method}')
    if form.validate_on_submit():
        app.logger.info('attempted logon')
        flash( f'Login requested for {form.username.data},' + \
               f' remember me={form.remember_me.data}. ')
        redirect('/index')
    return render_template( 'login.html',  form=form)