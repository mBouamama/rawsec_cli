"""Test file for searchCommand File"""
from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from rawsec_cli.cli.cli import cli


class TestSearchCommand(TestCase):
    """Test searchCommand class"""

    def setUp(self):
        """setup test"""
        self.json = {
            "tools": {
                "binary_exploitation": {
                    "tools": [{"name": "tools", "website": "test"}],
                },
            },
            "resources": {
                "binary_exploitation": {"resources": [{"name": "resources"}]},
            },
            "operating_systems": {
                "binary_exploitation": {
                    "operating_systems": [{"os": "operating_systems"}],
                },
            },
            "ctf_platforms": {
                "binary_exploitation": {
                    "ctf_platforms": [{"name": "ctf_platforms"}],
                },
            },
        }

    @patch(
        "rawsec_cli.search.searchProject",
        return_value=[{"name": "tools", "website": "test"}],
    )
    def testSearch(self, m):
        """ test search function"""
        result = CliRunner().invoke(
            cli,
            ["search", "tools"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("tools", result.output)

    def testSearchOnly1Result(self):
        """ test search only 1 result function"""
        result = CliRunner().invoke(
            cli,
            ["search", "myjwt"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("myjwt", result.output)

        result = CliRunner().invoke(
            cli,
            ["search", "wfuzz"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("wfuzz", result.output)

    def testSearchNotFound(self):
        """ test search incorrect project function"""
        result = CliRunner().invoke(
            cli,
            ["search", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"],
            catch_exceptions=False,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Project not found!", result.output)