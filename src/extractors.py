import re


def extract_markdown_images(markdown: str):
    result = []
    alt_texts = re.findall(r"\!\[(.*?)\]", markdown)
    links = re.findall(r"\((.*?)\)", markdown)

    for alt_text, link in zip(alt_texts, links):
        result.append((alt_text, link))

    return result


def extract_markdown_links(markdown: str):
    result = []
    anchor_texts = re.findall(r"\[(.*?)\]", markdown)
    links = re.findall(r"\((.*?)\)", markdown)

    for anchor_text, link in zip(anchor_texts, links):
        result.append((anchor_text, link))

    return result
