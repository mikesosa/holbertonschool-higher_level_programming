#!/usr/bin/python3
""" Unit tests for models/base.py """
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def test_int(self):
        x = Base(33)
        self.assertEqual(x.id, 33)
        x = Base(11)
        self.assertEqual(x.id, 11)

    def test_float(self):
        x = Base(3)
        self.assertEqual(x.id, 3)
        x = Base(3.4)
        self.assertEqual(x.id, 3.4)

    def test_strings(self):
        x = Base(1)
        self.assertEqual(x.id, 1)
        x = Base("34")
        self.assertEqual(x.id, "34")

    def test_empty(self):
        x = Base()
        self.assertEqual(x.id, 1)
        x = Base(7)
        self.assertEqual(x.id, 7)
        x = Base(None)
        self.assertEqual(x.id, 2)
        x = Base()
        self.assertEqual(x.id, 3)

    def test_weird(self):
        """ test wtf things """
        x = Base(4)
        self.assertEqual(4, x.id)
        x = Base([1, 2])
        self.assertEqual([1, 2], x.id)
        x = Base([1, "2"])
        self.assertEqual([1, '2'], x.id)
        x = Base([1, [1, 2]])
        self.assertEqual([1, [1, 2]], x.id)
        x = Base({"goku": 2})
        self.assertEqual({"goku": 2}, x.id)
        x = Base((1, 2))
        self.assertEqual((1, 2), x.id)
        x = Base(1)
        self.assertEqual(1, x.id)
        x = Base()
        self.assertEqual(4, x.id)
