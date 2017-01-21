# project/tests/test.py

import unittest

from project import app

class ProjectTests(unittest.TestCase):

    # Setup and teardown
    # executed prior each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    # Helper Methods

    #####

    # Tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the Kumpulan!', response.data)
        self.assertIn(b'Search your hang-out places with your communities here!', response.data)
        self.assertIn(b'Search Community', response.data)
        self.assertIn(b'Search Place', response.data)
        self.assertIn(b'Places Near You', response.data)
        
if __name__ == "__main__":
    unittest.main()
