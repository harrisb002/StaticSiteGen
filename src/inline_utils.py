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


def split_nodes_image(old_nodes):
    split_text_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            split_text_nodes.append(node)
            continue

        text_urls = extract_markdown_images(node.text)  # Extract images
        if len(text_urls) == 0:
            split_text_nodes.append(node)
            continue

        raw_text = node.text  # Start with the full text

        # Replace image syntax with a placeholder
        for txt, url in text_urls:
            raw_text = raw_text.replace(f"![{txt}]({url})", "!")

        text_parts = raw_text.split("!")  # Split text by the placeholders

        for i, part in enumerate(text_parts):
            if part:  # Add normal text nodes if text exists
                split_text_nodes.append(TextNode(part, TextType.NORMAL))
            if i < len(text_urls):  # Ensure an image exists at this index
                alt_text, url = text_urls[i]
                split_text_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

    return split_text_nodes


def split_nodes_link(old_nodes):
    split_text_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            split_text_nodes.append(node)
            continue

        text_urls = extract_markdown_links(node.text)  # Extract links
        if len(text_urls) == 0:
            split_text_nodes.append(node)
            continue

        raw_text = node.text  # Start with the full text

        # Replace link syntax with a placeholder
        for txt, url in text_urls:
            raw_text = raw_text.replace(f"[{txt}]({url})", "!")

        text_parts = raw_text.split("!")  # Split text by the placeholders

        for i, part in enumerate(text_parts):
            if part:  # Add normal text nodes if text exists
                split_text_nodes.append(TextNode(part, TextType.NORMAL))
            if i < len(text_urls):  # Ensure a link exists at this index
                link_text, url = text_urls[i]
                split_text_nodes.append(TextNode(link_text, TextType.LINK, url))

    return split_text_nodes
