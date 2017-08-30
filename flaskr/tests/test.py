# project/test.py
"""
This is 'test.py' - used to run a few unit tests on the code
""" 
import unittest
from flaskr import flaskrapp
 
class ProjectTests(unittest.TestCase):
"""
setup and teardown
"""
    def setUp(self):
    # executed prior to each test
        flaskrapp.config['TESTING'] = True
        flaskrapp.config['DEBUG'] = False
        self.flaskrapp = flaskrapp.test_client()
 
        self.assertEquals(flaskrapp.debug, False)
 
    def tearDown(self):
    # executed after each test
        pass
 
    # helper methods
 
    ###############
    #### tests ####
    ###############
 
    def test_index_page(self):
    # Test the index page text
        response = self.flaskrapp.get('/', follow_redirects=True)
        self.assertIn(b'Flaskr', response.data)
        self.assertIn(b'A simple Flask app.', response.data)
 
if __name__ == "__main__":
    unittest.main()
