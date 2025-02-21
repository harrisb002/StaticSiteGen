import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_conversion(self):
        text_node = TextNode("Hello, world!", TextType.NORMAL)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.to_html(), "Hello, world!")

    def test_bold_conversion(self):
        text_node = TextNode("Bold Text", TextType.BOLD)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.to_html(), "<b>Bold Text</b>")

    def test_italic_conversion(self):
        text_node = TextNode("Italic Text", TextType.ITALIC)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.to_html(), "<i>Italic Text</i>")

    def test_code_conversion(self):
        text_node = TextNode("print('Hello')", TextType.CODE)
        result = text_node_to_html_node(text_node)
        self.assertEqual(result.to_html(), "<code>print('Hello')</code>")

    def test_link_conversion(self):
        text_node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
        result = text_node_to_html_node(text_node)
        self.assertEqual(
            result.to_html(), '<a href="https://www.boot.dev">Click me</a>'
        )

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            text_node = TextNode("Invalid", "UNKNOWN")
            text_node_to_html_node(text_node)

    def test_link_missing_url(self):
        with self.assertRaises(ValueError):
            text_node = TextNode("Click here", TextType.LINK)
            text_node_to_html_node(text_node)

    def test_image_missing_url(self):
        with self.assertRaises(ValueError):
            text_node = TextNode("Alt text", TextType.IMAGE)
            text_node_to_html_node(text_node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
