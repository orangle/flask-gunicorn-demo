#!/usr/bin/env python
"""
This is 'run.py' - it calls the run() function for the instance
of the Flask module that was created in the 'flaskr.py' file.
"""

from flaskr import application

if __name__ == "__main__":
    application.run()
