#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def Test_Max_list_firt(self):
        my_list = [23, 19, 10, 6]
        self.assertEqual(max_integer(my_list), 23)

    def Test_Max_list_last(self):
        my_list = [3, 7, 16, 23]
        self.assertEqual(max_integer(my_list), 23)

    def Test_Empty_List(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def Test_mixed_list(self):
        my_list = [5, -5, -9, 12]
        self.assertEqual(max_integer(my_list), 12)

    def test_Max_integer_with_string(self):
        my_list = ["hi", 12, 13, -5]
        with self.assertRaises(TypeError):
            max_integer(my_list)
