from src.textnode import TextNode, TextType
import re

# Accepts an array of htmlnodes
# Returns a new list of nodes, where any "text" type nodes are split based on type
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # If it's not a text node, add it as is
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # If uneven num of parts, Markdown invalid
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: Unmatched {delimiter}")

        # Iterate through split parts and alternate between normal and the given text type
        for i, part in enumerate(parts):
            if part or i % 2 == 1:  # Preserve empty text nodes
                new_nodes.append(
                    # Only odd is text_type
                    TextNode(part, text_type if i % 2 == 1 else TextType.NORMAL)
                )

    return new_nodes


def extract_markdown_images(text):
    """Extracts image alt text and URLs from markdown."""
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """Extracts link text and URLs from markdown."""
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)