#!/usr/bin/env python3
'''Parameterize a unit test
'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self, input1, input2, expected):
        '''test has_licence method
        '''
        myclass = GithubOrgClient("args")
        self.assertIs(myclass.has_license(input1, input2), expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration testing."""
        def side(url):
            """Side effect function for requests.get mock."""
            repo = []
            mock_response = Mock()
            for payload in TEST_PAYLOAD:
                if url == payload[0]["repos_url"]:
                    repo = payload[1]
                    break
            mock_response.json.return_value = repo
            return mock_response
        cls.get_patcher = patch('requests.get', side_effect=side)
        cls.org_patcher = patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock,
                return_value=cls.org_payload)
        cls.get_patcher.start()
        cls.org_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after integration testing."""
        cls.get_patcher.stop()
        cls.org_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method without specifying a license."""
        inst = GithubOrgClient('google/repos')
        self.assertEqual(inst.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with a specified license."""
        inst = GithubOrgClient('google/repos')
        self.assertEqual(inst.public_repos(license="apache-2.0"),
                         self.apache2_repos)
