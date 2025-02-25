import unittest

from src.htmlnode import HTMLNode, ParentNode, LeafNode


# tag=None, value=None, children=None, props=None
class TestHTMLNode(unittest.TestCase):

    def test_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(props={"id": "header"})
        self.assertEqual(node.props_to_html(), ' id="header"')

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_parent_node_requires_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("p", "Hello!")])
        self.assertEqual(str(context.exception), "All Parent nodes must have a tag")

    def test_parent_node_requires_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [])
        self.assertEqual(
            str(context.exception), "All Parent nodes require at least one child"
        )

    def test_parent_node_basic_html(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

    def test_parent_node_multiple_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "First paragraph."),
                LeafNode("p", "Second paragraph."),
            ],
        )
        self.assertEqual(
            node.to_html(), "<div><p>First paragraph.</p><p>Second paragraph.</p></div>"
        )

    def test_parent_node_nested(self):
        node = ParentNode(
            "section",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("p", "Nested paragraph."),
                        LeafNode("b", "Bold text."),
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<section><div><p>Nested paragraph.</p><b>Bold text.</b></div></section>",
        )

    def test_parent_node_with_attributes(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Styled text.")],
            props={"class": "container", "id": "main"},
        )
        self.assertEqual(
            node.to_html(), '<div class="container" id="main"><p>Styled text.</p></div>'
        )

    def test_parent_node_with_text_and_inline_tags(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " normal "),
                LeafNode("i", "italic"),
                LeafNode(None, " text."),
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><b>Bold</b> normal <i>italic</i> text.</p>"
        )

    def test_deeply_nested_structure(self):
        node = ParentNode(
            "article",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "div",
                            [
                                LeafNode("h1", "Title"),
                                ParentNode(
                                    "p", [LeafNode(None, "Deeply nested text.")]
                                ),
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<article><section><div><h1>Title</h1><p>Deeply nested text.</p></div></section></article>",
        )

    def test_parent_node_repr(self):
        node = ParentNode("div", [LeafNode("p", "Content")], props={"class": "box"})
        self.assertEqual(
            repr(node),
            "HTMLNode(div, None, children: [HTMLNode(p, Content, children: None, None)], {'class': 'box'})",
        )

    def test_parent_node_mixed_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                ParentNode(
                    "span",
                    [LeafNode(None, "Inline text.")],
                    props={"class": "highlight"},
                ),
                LeafNode(None, " Normal text."),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold</b><span class="highlight">Inline text.</span> Normal text.</p>',
        )


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
