from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    # return '<h2>Hello, World!</h2>'
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h2>Hello, dear {}!</h2>'.format(name)
