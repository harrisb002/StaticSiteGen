import os
import shutil


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
