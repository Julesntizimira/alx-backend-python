#!/usr/bin/env python3
'''Parameterize a unit test
'''
from utils import access_nested_map
import unittest
from parameterized import parameterized



class TestAccessNestedMap(unittest.TestCase):
    '''test utils.access_nested_map
    '''
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, input1, input2, expected):
        '''test case access_nested_map
        '''
        self.assertEqual(access_nested_map(input1, input2), expected)
        
    @parameterized.expand([({}, ("a",), "a"),({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, input1, input2, expected_msg):
        '''test exception
        '''
        with self.assertRaises(KeyError, msg=expected_msg):
            access_nested_map(input1, input2)
