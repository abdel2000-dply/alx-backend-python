#!/usr/bin/env python3
'''tests for client.py'''
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_licence", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        '''test has_license method'''
        client = GithubOrgClient('github')
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''TestIntegrationGithubOrgClient class'''
    @classmethod
    def setUpClass(cls):
        '''setUpClass method'''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            '''side_effect'''
            if url == 'https://api.github.com/orgs/github':
                return cls.org_payload
            if url == 'https://api.github.com/orgs/github/repos':
                return cls.repos_payload
            return None
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        '''tearDownClass method'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public_repos method"""
        github_org_client = GithubOrgClient("github")
        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """test public_repos method with license"""
        github_org_client = GithubOrgClient("github")
        self.assertEqual(github_org_client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
