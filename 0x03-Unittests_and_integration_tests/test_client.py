#!/usr/bin/env python3
'''tests for client.py'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        '''test public_repos_url method'''
        payload = {'repos_url': 'https://api.github.com/orgs/github/repos'}
        mock_org.return_value = payload
        client = GithubOrgClient('github')
        self.assertEqual(client._public_repos_url, payload['repos_url'])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_repo_url, mock_get_json):
        '''test public_repos method'''
        mock_repo_url.return_value = 'https://api.github.com/orgs/github/repos'
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        client = GithubOrgClient('github')
        self.assertEqual(client.public_repos(), ['repo1', 'repo2'])
        mock_get_json.assert_called_once()
        mock_repo_url.assert_called_once()
