import sys

from cp_rec import cp_files
from generate_page import generate_page, generate_pages_recursive


def main():
    basepath = sys.argv[1] if sys.argv[1] else "/"
    cp_files("static", "docs")
    generate_pages_recursive(basepath, "template.html", "docs")


main()
