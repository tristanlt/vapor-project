import unittest
import pytest
from flask import Flask

from vapor import vapor

class VaporMethods(unittest.TestCase):
    def setUp(self):
        vapor.app.testing = True
        self.app = vapor.app.test_client()

    def test_sum(self):
        self.assertEqual(vapor.sumit(1,3), 4)

    def test_root(self):
        r = self.app.get('/')
        self.assertEqual(r.data, "There is nothing here")

if __name__ == '__main__':
        unittest.main()
