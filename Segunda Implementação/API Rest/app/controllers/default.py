from app import app
from flask import render_template

from app.models.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    loginForm = LoginForm()

    if(loginForm.validate_on_submit()):
        print(loginForm.username.data)
        print(loginForm.password.data)
        print(loginForm.remember_me.data)
    else:
        print(loginForm.errors)

    return render_template('login.html', form=loginForm)