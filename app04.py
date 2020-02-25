from flask import abort, Flask, redirect, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('about', next='/path/to'))

@app.route('/projects/')
def projects():
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    abort(401)