from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from inline_utils import split_nodes_delimiter, extract_markdown_links, extract_markdown_images


def main():
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)

    # text_node = TextNode("Click me", "link", "https://www.boot.dev")
    # html_node = HTMLNode(
    #     tag="a",
    #     value=text_node.text,
    #     props={"href": "https://www.google.com", "target": "_blank"},
    # )
    # print(html_node.props_to_html())

    # text_node = TextNode("Click me", "link", "https://www.boot.dev")
    # text_node_to_html(text_node)

    TestleafNode = LeafNode("p", "This is a paragraph of text.")
    TestleafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(TestleafNode.to_html())  # <p>This is a paragraph of text.</p>
    print(TestleafNode2.to_html())  # <a href="https://www.google.com">Click me!</a>


if __name__ == "__main__":
    main()
