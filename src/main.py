from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

    text_node = TextNode("Click me", "link", "https://www.boot.dev")
    html_node = HTMLNode(
        tag="a",
        value=text_node.text,
        props={"href": "https://www.google.com", "target": "_blank"},
    )
    print(html_node.props_to_html())


if __name__ == "__main__":
    main()
