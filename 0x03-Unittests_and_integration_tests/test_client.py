#!/usr/bin/env python3
'''Parameterize a unit test
'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test class
       GithubOrgClient
    '''
    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name: str, mocked_get_json: Mock):
        """Test the org method of GithubOrgClient."""
        inst = GithubOrgClient(org_name)
        inst.org
        mocked_get_json.assert_called_once_with(
            inst.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        '''mock a property
        '''
        mocked_property = PropertyMock(return_value={"repos_url":
                                                     "mocked property"})
        with patch.object(GithubOrgClient, 'org', mocked_property):
            myclass = GithubOrgClient("args")
            self.assertEqual(myclass._public_repos_url, "mocked property")

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        '''test public_repos
        '''
        mylist = [{"name": "jules", "licence": "43567"}]
        mocked_property = PropertyMock(return_value=mylist)
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          mocked_property):
            mocked_get_json.return_value = mocked_property.return_value
            myclass = GithubOrgClient("args")
            self.assertEqual(myclass.public_repos(), ["jules"])
            mocked_property.assert_called_once()
            mocked_get_json.assert_called_once()
