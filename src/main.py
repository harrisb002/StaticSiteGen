import os
import shutil
from web import copy_static, generate_pages_recursive


def main():
    public_dir = "public"
    static_dir = "static"
    content_dir = "content"
    template_file = "template.html"

    # Delete anything in the public directory
    print("Cleaning up the public directory...")
    if os.path.exists(public_dir):
        for filename in os.listdir(public_dir):
            file_path = os.path.join(public_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    # Copy all static files from static to public
    print("Copying static files...")
    copy_static(static_dir, public_dir)

    # Generate all markdown pages recursively
    print("Generating HTML pages from markdown...")
    generate_pages_recursive(content_dir, template_file, public_dir)

    print("Static site generation complete!")


if __name__ == "__main__":
    main()
