import os
import shutil
import re
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    """
    Recursively generates HTML pages from markdown files in the content directory.

    - Crawls every entry in `dir_path_content`
    - Converts markdown files into HTML using `template_path`
    - Writes the output to `dest_dir_path`, preserving the directory structure.

    :param dir_path_content: Path to the content directory containing markdown files.
    :param template_path: Path to the HTML template file.
    :param dest_dir_path: Path to the destination directory where HTML files will be written.
    """
    for root, _, files in os.walk(dir_path_content):
        # Determine the relative path from the content directory
        relative_path = os.path.relpath(root, dir_path_content)
        dest_path = os.path.join(dest_dir_path, relative_path)

        # Ensure the destination directory exists
        os.makedirs(dest_path, exist_ok=True)

        for file in files:
            if file.endswith(".md"):
                markdown_file = os.path.join(root, file)
                html_file = os.path.join(dest_path, file.replace(".md", ".html"))

                print(
                    f"Generating {html_file} from {markdown_file} using {template_path}"
                )
                generate_page(markdown_file, template_path, html_file)


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
