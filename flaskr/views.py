#!/usr/bin/env python
# File: flaskr/views.py

# imports
from flaskr import flaskrapp
from flask import render_template
from flask import request

# routes
@flaskrapp.route('/')
@flaskrapp.route('/index')
def index():
    return render_template('index.html')
