import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


if __name__ == "__main__":
    unittest.main()
