#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from 1 import greaterthan

class TestGreaterThan(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [3, 2]
        result = greaterthan(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
