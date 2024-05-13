#!/usr/bin/env python3
'''tests for utils.py'''
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''tests for access_nested_map'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''method for testing access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''test for access_nested_map exception'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''tests for get_json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        '''test get_json
        patch, to avoid making an actual HTTP request
        mock, to create a mock object for the response
        '''
        with patch('requests.get') as mock:
            mock.return_value = Mock(json=lambda: test_payload)
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''tests for memoize'''
    def test_memoize(self):
        '''test memoize'''
        class TestClass:
            def a_method(self):
                '''a method'''
                return 42

            @memoize
            def a_property(self):
                '''a property'''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock.assert_called_once()
