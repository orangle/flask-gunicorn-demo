#!/usr/bin/env python
# File: flaskr/__init__.py
"""
This is '__init__.py' - Entry point into the application
"""

# imports
from flask import Flask

# configuration
flaskrapp = Flask(__name__, instance_relative_config=True) # pylint: disable=invalid-name
from flaskr import views # pylint: disable=wrong-import-position

flaskrapp.config.from_object('config')
