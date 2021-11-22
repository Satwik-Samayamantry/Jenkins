#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from code import greaterthan

class TestGreaterThan(unittest.TestCase):
    def test1(self):
        a = 3
        b = 2
        result = greaterthan(a,b)
        self.assertEqual(result, 1)
        
    def test2(self):
        a = 2
        b = 3
        result = greaterthan(a,b)
        self.assertEqual(result, 0)
      
    def test3(self):
        a = 3
        b = 3
        result = greaterthan(a,b)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
