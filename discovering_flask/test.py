from main import app
from flask import request, render_template
import unittest


class TestFlaskApp(unittest.TestCase):
    LOGIN_URL = '/login'
    HOME_URL = '/'
    render_templates = False
    @classmethod
    def setUp(cls):
        print('Running setup')
        cls.app = app.test_client()
        cls.app.testing = True

    def tearDown(self):
        pass

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Nothing')

    def test_welcome(self):
        result = self.app.get('/welcome', content_type='html/text')
        self.assertEqual(result.status_code, 302)

    def test_login(self):
        result = self.app.post('/login', content_type='html/text')
        self.assertEqual(result.status_code, 400)
        self.assertTrue(b'Please login' in result.data)
