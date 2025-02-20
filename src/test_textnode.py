import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is the same text node", TextType.BOLD)
        node2 = TextNode("This is the same text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/tracks/backend")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/tracks/backend")
        self.assertEqual(node, node2)
    
    def test_type_not_eq(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/tracks/backend")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/tracks/frontend")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()