from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', name = name )

