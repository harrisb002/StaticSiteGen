import os
import shutil
import re
from markdown_blocks import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):
    """
    Generates an HTML page from a markdown file using a template.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def extract_title(markdown: str) -> str:
    """
    Extracts the H1 header from a markdown string.
    If there is no H1 header, raises a ValueError.
    """
    match = re.search(r"^#\s*(.+)", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    raise ValueError("No H1 header found in the markdown")


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

    # Recreate destination directory
    os.mkdir(destination)

    # Recursively copy contents
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)

        elif os.path.isdir(source_path):
            os.mkdir(destination_path)
            copy_static(
                source_path, destination_path
            )  # Recursively copy subdirectories
