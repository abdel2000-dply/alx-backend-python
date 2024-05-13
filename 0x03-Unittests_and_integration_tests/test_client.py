#!/usr/bin/env python3
'''tests for client.py'''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient class'''
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org_name, mock_get_json):
        '''test org method'''
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'payload': True})
        mock_get_json.assert_called_once()
