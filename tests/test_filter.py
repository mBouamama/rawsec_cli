"""Test file for filter File"""
from unittest import TestCase

from rawsec_cli.filter import filterProjects


class TestFilter(TestCase):
    """Test filter class"""
    def setUp(self):
        """setup test"""
        self.projects = [
            {
                "name": "test",
                "description": "a",
                "language": "Python",
                "price": "Paid",
                "online": "True",
                "blackarch": "test",
            },
            {
                "name": "test2",
                "description": "ab",
                "language": "Go",
                "price": "Free",
                "online": "False",
                "blackarch": "test",
            },
        ]

    def testFilterProjects(self):
        """ test FilterProjects function"""
        projects = filterProjects(
            self.projects,
            lang="Python",
            price=True,
            online=True,
            blackarch=True,
        )
        self.assertEqual(projects, [self.projects[0]])

        projects = filterProjects(
            self.projects,
            lang="Go",
            free=True,
            offline=True,
            blackarch=True,
        )
        self.assertEqual(projects, [self.projects[1]])
