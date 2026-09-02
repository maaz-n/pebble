from extractors import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_links(original_text)

        if node.text_type != TextType.TEXT or not links:
            result.append(node)
            continue

        for link_tuple in links:
            link_anchor = link_tuple[0]
            link_url = link_tuple[1]
            sections = original_text.split(f"[{link_anchor}]({link_url})", maxsplit=1)
            text = sections[0]
            if text:
                # it is simple text
                result.append(TextNode(text, TextType.TEXT))
            result.append(TextNode(link_anchor, TextType.LINK, link_url))
            original_text = sections[1]
        if original_text:
            result.extend([TextNode(original_text, TextType.TEXT)])

    return result


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for node in old_nodes:
        original_text = node.text
        images = extract_markdown_images(original_text)

        if node.text_type != TextType.TEXT or not images:
            result.append(node)
            continue

        for image_tuple in images:
            image_alt = image_tuple[0]
            image_url = image_tuple[1]
            sections = original_text.split(f"![{image_alt}]({image_url})", maxsplit=1)
            text = sections[0]
            if text:
                # it is simple text
                result.append(TextNode(text, TextType.TEXT))
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            if len(sections) > 1:
                original_text = sections[1]
        if original_text:
            result.extend([TextNode(original_text, TextType.TEXT)])

    return result
