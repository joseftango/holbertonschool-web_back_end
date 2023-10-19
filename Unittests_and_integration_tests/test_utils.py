#!/usr/bin/env python3
"""test_utils module"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """class named TestAccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])

    def test_access_nested_map(self, nested_map, path, result):
        """test_access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)
    
    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested_map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested_map")
        ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """test_access_nested_map_exception method"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(result, e.exception)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock HTTP calls"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize(self):
        """ Tests memoize method """

        class TestClass:
            """TestClass"""

            def a_method(self):
                """ Method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test = TestClass()
            result = test. a_property
            result = test. a_property
            self.assertEqual(result, 42)
            mocked.assert_called_once()
