import os
from web import copy_static, generate_page


def main():
    public_dir = "public"
    static_dir = "static"
    markdown_file = "content/index.md"
    template_file = "template.html"
    output_file = os.path.join(public_dir, "index.html")

    # Step 1: Delete anything in the public directory
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

    # Step 2: Copy all static files from static to public
    print("Copying static files...")
    copy_static(static_dir, public_dir)

    # Step 3: Generate the page from content/index.md using template.html
    print("Generating HTML page from markdown...")
    generate_page(markdown_file, template_file, output_file)

    print("Static site generation complete!")


if __name__ == "__main__":
    main()
