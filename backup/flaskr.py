#!/usr/bin/env python
"""
This is 'flaskr.py' - our main function that defines the default
route ('/') and prints a test message on the browser.
"""

from flask import Flask
application = Flask(__name__) # pylint: disable=invalid-name

@application.route("/")
def hello():
    """
    Defines the route ('/') and what needs to be returned.
    """
    return "<h1 style='color:blue'>Hello World!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
