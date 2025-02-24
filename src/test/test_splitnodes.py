import unittest
from src.textnode import TextNode, TextType
from src.inline_utils import split_nodes_image, split_nodes_link


class TestSplitNodesDelimiter(unittest.TestCase):

    # One image in the text
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    # Single image with no surrounding text
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    # Multiple images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    # Node has no image
    def test_split_image_no_images(self):
        node = TextNode(
            "This is just normal text with no image.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is just normal text with no image.", TextType.NORMAL)],
            new_nodes,
        )

    # One link in the text
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.NORMAL),
            ],
            new_nodes,
        )

    # Node has no links
    def test_split_links_no_links(self):
        node = TextNode(
            "This is just normal text with no links.",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is just normal text with no links.", TextType.NORMAL)],
            new_nodes,
        )

    # Node has both links and images
    def test_split_links_and_images(self):
        node = TextNode(
            "This is an image ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])  # First split the image
        new_nodes = split_nodes_link(new_nodes)  # Then split the links
        self.assertListEqual(
            [
                TextNode("This is an image ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(".", TextType.NORMAL),
            ],
            new_nodes,
        )

    # Node is a non-text node (e.g., bold or italic)
    def test_non_text_nodes(self):
        node = TextNode(
            "This is **bold** and _italic_ text.",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is **bold** and _italic_ text.", TextType.BOLD)],
            new_nodes,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is **bold** and _italic_ text.", TextType.BOLD)],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
