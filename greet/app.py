from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def say_welcome():
    return "Welcome"


@app.route('/welcome/home')
def say_welcome_home():
    return "Welcome home"


@app.route('/welcome/back')
def say_welcome_back():
    return "Welcome back"

# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”
