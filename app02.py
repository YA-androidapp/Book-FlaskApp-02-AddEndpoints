from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/user/name/<username>')
def show_name(username):
    return 'Name %s' % escape(username)

@app.route('/user/age/<int:age>')
def show_age_int(age):
    return 'Age %d' % age

@app.route('/user/age/<float:age>')
def show_age_float(age):
    return 'Age %f' % age

@app.route('/user/height/<float:height>')
def show_height(height):
    return 'Height %f' % height

@app.route('/user/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/user/id/<uuid:id>')
def show_id(id):
    return 'ID %s' % id