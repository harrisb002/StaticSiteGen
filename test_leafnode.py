import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_valid_leafnode(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_leafnode_with_props(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')

    def test_leafnode_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leafnode_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)


if __name__ == "__main__":
    unittest.main()
