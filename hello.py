#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os
import sys
from flask import Flask, render_template
from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bad')
def bad():
    return '<h1>Bad Request</h1>', 400

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()