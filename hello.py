from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Hello, World!</h2>'


@app.route('/user/<name>')
def user(name):
    return '<h2>Hello, dear {}!</h2>'.format(name)
