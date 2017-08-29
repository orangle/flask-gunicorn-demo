# project/test.py
 
import unittest
from flaskr import flaskrapp
 
class ProjectTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        flaskrapp.config['TESTING'] = True
        flaskrapp.config['DEBUG'] = False
        self.flaskrapp = flaskrapp.test_client()
 
        self.assertEquals(flaskrapp.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
    ########################
    #### helper methods ####
    ########################
 
 
 
    ###############
    #### tests ####
    ###############
 
    def test_index_page(self):
        response = self.flaskrapp.get('/', follow_redirects=True)
        self.assertIn(b'Flaskr', response.data)
<<<<<<< HEAD
        self.assertIn(b'A simple Flask cow.', response.data)
=======
        self.assertIn(b'A simple Flask app.', response.data)
>>>>>>> a2e8baeb433690d6ace32f8649dd21b85c73ae53
 
 
if __name__ == "__main__":
    unittest.main()
