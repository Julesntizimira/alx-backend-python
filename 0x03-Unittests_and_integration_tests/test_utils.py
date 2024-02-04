#!/usr/bin/env python3
'''Parameterize a unit test
'''
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''test utils.access_nested_map
    '''
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, input1, input2, expected):
        '''test case access_nested_map
        '''
        self.assertEqual(utils.access_nested_map(input1, input2), expected)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, input1, input2, expected_msg):
        '''test exception
        '''
        with self.assertRaises(KeyError, msg=expected_msg):
            utils.access_nested_map(input1, input2)


class TestGetJson(unittest.TestCase):
    '''test GetJson
    '''
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, input_param, expected):
        '''test get method
        '''
        with patch('utils.requests.get') as mock_object:
            mock_response1 = Mock()
            mock_response1.json.return_value = {"payload": True}
            mock_response2 = Mock()
            mock_response2.json.return_value = {"payload": False}
            if input_param == 'http://example.com':
                mock_object.return_value = mock_response1
            elif input_param == 'http://holberton.io':
                mock_object.return_value = mock_response2
            self.assertEqual(utils.get_json(input_param), expected)
