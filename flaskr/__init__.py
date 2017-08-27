#!/usr/bin/env python
# File: flaskr/__init__.py

# imports
from flask import Flask

# configuration
flaskrapp = Flask(__name__)
from flaskr import views
