import os
import unittest
import tempfile

from .. import app
from ..database import init_db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['db'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            init_db()

    def tearDown(self):
        pass
