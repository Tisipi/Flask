from flask import Flask
from flask import render_template

from flask import request
from flask import redirect


app = Flask(__name__)


@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is {}. Headers are: {} </p>'.format(user_agent, request.headers)
    # return redirect('http://www.docker.com')
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h2>Hello, dear {}!</h2>'.format(name)
    return render_template('user.html', name=name)

