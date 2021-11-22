#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from code import greaterthan

class TestGreaterThan(unittest.TestCase):
    def test_list_int(self):
       
        a = 3
        b = 2
        result = greaterthan(a,b)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
