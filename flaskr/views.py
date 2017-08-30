#!/usr/bin/env python
# File: flaskr/views.py
"""
This is 'views.py' - which uses decorators to generate views.
"""

# imports
from flaskr import flaskrapp # pylint: disable=invalid-name
from flask import render_template
from flask import request

# routes
@flaskrapp.route('/')
@flaskrapp.route('/index')
def index():
    """
    Function index(), to render the index file
    """
    return render_template('index.html')
