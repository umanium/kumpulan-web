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
    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        print('\nTesting the user page')
        self.assertIn(b'There will be something here', response.data)

if __name__ == "__main__":
    unittest.main()
