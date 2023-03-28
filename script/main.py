import requests
import unittest
from unittest import TestCase

class TestRequests(TestCase):
    def setUp(self):
        self.req=requests.get('https://python-microblog-w8bz.onrender.com/')

    def test_get(self):
        assert(self.req.status_code==200)

    def test_post(self):
        self.assertTrue(self.req==500)


 