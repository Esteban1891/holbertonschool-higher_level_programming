#!/usr/bin/python3
"""unit testing for max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """[TestMaxInteger class]
    Arguments:
        unittest {[builtin]} -- [built in to unit testing]
    """
    def test_empty_list(self):
        """test if list is empty
        """
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_max_at_start(self):
        """test if max int at start
        """
        max_list = [10, 6, 5, 2]
        self.assertEqual(max_integer(max_list), 10)

    def test_max_at_middle(self):
        """test if max at middle
        """
        max_list = [10, 9, 15, 4, 2]
        self.assertEqual(max_integer(max_list), 15)

    def test_max_negative(self):
        """test if max is negative number
        """
        max_list = [-5, -10, -9, -1, -2]
        self.assertEqual(max_integer(max_list), -1)

    def test_strings_with_ints(self):
        """test with mixed types
        """
        max_list = ["hi", "hello", 5]
        with self.assertRaises(TypeError):
            max_integer(max_list)

    def test_float_and_int(self):
        """test floats and ints
        """
        max_list = [3.4, 14, 66.66, 11]
        self.assertEqual(max_integer(max_list), 66.66)

    def test_floats_only(self):
        """test for floats only
        """
        max_list = [1.1, 12.2, 14.5, 6.3]
        self.assertEqual(max_integer(max_list), 14.5)

    def test_strings_only(self):
        """test for strings only
        """
        max_list = ["hi", "hello", "hello"]
        self.assertNotEqual(max_integer(max_list), "hello")

    def test_long_int(self):
        """testing a long int
        """
        max_list = [99999999999999, 5, 2]
        self.assertEqual(max_integer(max_list), 99999999999999)

    def test_string(self):
        """test string instead of list
        """
        max_string = "hello"
        self.assertEqual(max_integer(max_string), 'o')

if __name__ == "__main__":
    unittest.main()

