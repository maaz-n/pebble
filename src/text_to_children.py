from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node


def text_to_children(text: str):
    result = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return result
