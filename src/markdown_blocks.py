import re
from html_node import ParentNode
from text_node import TextNode, text_node_to_html_node
from split_blocks import markdown_to_blocks, BlockType, block_to_block_type
from inline_utils import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        if html_node:
            children.append(html_node)
    return ParentNode("div", children, None) if children else None


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if not block.strip():
        return None

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(line.strip() for line in lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.strip().split("\n")
    html_items = []
    for item in items:
        text = re.sub(r"^\d+\.\s*", "", item)
        if text:
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.strip().split("\n")
    html_items = []
    for item in items:
        text = re.sub(r"^[-*]\s*", "", item)
        if text:
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = [
        re.sub(r"^>\s?", "", line).strip()
        for line in lines
        if line.strip().startswith(">")
    ]

    if not new_lines:
        raise ValueError("invalid quote block")

    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
