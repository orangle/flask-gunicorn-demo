# project/test.py
 
import unittest
from flaskr import application 
 
class ProjectTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        application.config['TESTING'] = True
        application.config['DEBUG'] = False
        self.application = app.test_client()
 
        self.assertEquals(application.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
    ########################
    #### helper methods ####
    ########################
 
 
 
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        response = self.application.get('/', follow_redirects=True)
        self.assertIn(b'Hello', response.data)
        self.assertIn(b'World', response.data)
 
 
if __name__ == "__main__":
    unittest.main()
