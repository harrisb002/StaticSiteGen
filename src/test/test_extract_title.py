import unittest
from src.web import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_valid_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#   Trimmed Title   "), "Trimmed Title")

    def test_missing_h1(self):
        with self.assertRaises(ValueError):
            extract_title("No header")
        with self.assertRaises(ValueError):
            extract_title("## Subheader")

    def test_multiple_headers(self):
        self.assertEqual(
            extract_title(
                """# First Header
        ## Second Header
        # Another H1"""
            ),
            "First Header",
        )

    def test_h1_with_special_characters(self):
        self.assertEqual(extract_title("# Hello, World!"), "Hello, World!")
        self.assertEqual(extract_title("# **Bold Title**"), "**Bold Title**")
