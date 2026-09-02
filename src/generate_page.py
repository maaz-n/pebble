import os
from pathlib import Path

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, "r") as f:
        markdown += f.read()

    template = ""
    with open(template_path, "r") as f:
        template += f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    final_html = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    os.makedirs(dest_path, exist_ok=True)

    file_path = f"{dest_path}/index.html"

    with open(file_path, "w") as f:
        f.write(final_html)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
):
    content_path = Path(dir_path_content)
    md_files = list(content_path.glob("**/*.md"))

    for file in md_files:
        target_dir = "/".join(
            str(file).replace("content", dest_dir_path).split("/")[:-1]
        )
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(os.path.abspath(file.parent), file.name)
        generate_page(file_path, template_path, target_dir, basepath)

    print("\n---Generated files successfully---\n")
