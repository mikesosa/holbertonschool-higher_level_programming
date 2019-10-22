#!/usr/bin/python3
""" Unit tests for models/base.py """

from models.base import Base
import unittest


class Test_Base(unittest.TestCase):

    def test_simple(self):
        """ simplest test cases """
        x = Base(1)
        self.assertEqual(1, x.id)
        self.assertNotEqual(99, x.id)
        x = Base(99)
        self.assertEqual(x.id, 99)

    def test_InputErrors(self):
        """ tests for input error """
        with self.assertRaises(AttributeError):
            self.assertIsEqual(x(), 1)

    def test_empty(self):
        """ test empty conditions """
        x = Base()
        self.assertEqual(1, x.id)
        x = Base(None)
        self.assertEqual(2, x.id)
        x = Base(None)
        self.assertEqual(3, x.id)
        x = Base(7)
        self.assertEqual(7, x.id)

    def test_string(self):
        """ tests strings """
        x = Base(2)
        self.assertEqual(2, x.id)
        x = Base("2")
        self.assertEqual('2', x.id)

    def test_float(self):
        """ test floats """
        x = Base(3)
        self.assertEqual(3, x.id)
        x = Base(3.45)
        self.assertEqual(3.45, x.id)
        x = Base(-4.56)
        self.assertEqual(-4.56, x.id)

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
        x = Base({"perro": 2})
        self.assertEqual({"perro": 2}, x.id)
        x = Base((1, 2))
        self.assertEqual((1, 2), x.id)
        x = Base(1)
        self.assertEqual(1, x.id)
        x = Base()
        self.assertEqual(6, x.id)

    def test_more_errors(self):
        """ more error checking """
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('NaN'))
        self.assertNotEqual(float('NaN'), x.id)
        with self.assertRaises(ValueError):
            x = Base(float('bob'))
        with self.assertRaises(ValueError):
            x = Base(int('goku'))
        x = Base()
        self.assertEqual(4, x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base(float('inf'))
        self.assertEqual(float('inf'), x.id)
        x = Base()
        self.assertEqual(5, x.id)

        def test_id(self):
            """ tests the if id works properly """
            goku = Base()
            gokuID = goku.id
            goku2 = Base(69)
            goku3 = Base(100)
            goku4 = Base()
            self.assertTrue(gokuID, 1)
            self.assertEqual(gokuID, 1)
            self.assertFalse(gokuID, goku4.id)
            self.assertTrue(gokuID + 1, goku4.id)
            self.assertFalse(goku2, goku3)
            seld.assertEqual(goku3.id, 100)

        def test_class(self):
            """ tests subclass """
            goku = Base()
            self.assertTrue(issubclass(type(goku), Base))

        def test_to_json_string(self):
            pass

if __name__ == "__main__":
    unittest.main()
