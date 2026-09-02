from cp_rec import cp_files
from generate_page import generate_page, generate_pages_recursive


def main():
    cp_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()
