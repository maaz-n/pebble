import os
from pathlib import Path

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, "r") as f:
        markdown += f.read()

    template = ""
    with open(template_path, "r") as f:
        template += f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    final_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    os.makedirs(dest_path, exist_ok=True)

    file_path = f"{dest_path}/index.html"

    with open(file_path, "w") as f:
        f.write(final_html)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    content_path = Path(dir_path_content)
    md_files = list(content_path.glob("**/*.md"))

    for file in md_files:
        rel_path = os.path.relpath(file, dir_path_content)
        target_dir = os.path.join(dest_dir_path, os.path.dirname(rel_path))
        print(target_dir)
        return
        target_dir = "/".join(
            str(file).replace("content", dest_dir_path).split("/")[:-1]
        )
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(os.path.abspath(file.parent), file.name)
        generate_page(file_path, template_path, target_dir)

    print("\n---Generated files successfully---\n")
