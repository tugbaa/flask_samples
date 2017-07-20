from flask import Flask
app=Flask(__name__)


@app.route('/')
def index():
    return "Index Page"

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s' % name
