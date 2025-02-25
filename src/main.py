# from textnode import TextNode, TextType
# from htmlnode import HTMLNode, LeafNode
# from inline_utils import (
#     split_nodes_delimiter,
#     extract_markdown_links,
#     extract_markdown_images,
# )

import os
import shutil


def copy_static(source: str, destination: str) -> None:
    """
    Recursively copies all contents from the source directory to the destination directory.
    It first deletes all existing contents in the destination to ensure a clean copy.

    :param source: Path to the source directory.
    :param destination: Path to the destination directory.
    """
    # Ensure destination is clean
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Deleted existing directory: {destination}")

    # Recreate destination directory
    os.mkdir(destination)
    print(f"Created directory: {destination}")

    # Recursively copy contents
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {source_path} -> {destination_path}")
        elif os.path.isdir(source_path):
            os.mkdir(destination_path)
            print(f"Created directory: {destination_path}")
            copy_static(
                source_path, destination_path
            )  # Recursively copy subdirectories


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

    # TestleafNode = LeafNode("p", "This is a paragraph of text.")
    # TestleafNode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    # print(TestleafNode.to_html())  # <p>This is a paragraph of text.</p>
    # print(TestleafNode2.to_html())  # <a href="https://www.google.com">Click me!</a>

    print("Generating static site...")
    copy_static("static", "public")
    print("Static site generation complete!")


if __name__ == "__main__":
    main()
