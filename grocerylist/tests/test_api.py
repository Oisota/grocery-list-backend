import os
import unittest
import tempfile

from .. import app
from ..database import init_db

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DB'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DB'])

    def test_grocery_list_get(self):
        self.assertTrue(False)

    def test_grocery_list_post(self):
        self.assertTrue(False)

    def test_grocery_item_get(self):
        self.assertTrue(False)

    def test_grocery_item_put(self):
        self.assertTrue(False)

    def test_grocery_item_delete(self):
        self.assertTrue(False)
