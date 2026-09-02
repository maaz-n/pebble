from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        node_text_list = node.text.split(delimiter)
        if len(node_text_list) % 2 == 0:
            # no closing delimiter
            raise Exception("Closing delimiter not found!")

        else:
            for (
                i,
                text,
            ) in enumerate(node_text_list):
                if i % 2 == 0:
                    # simple text
                    if text:
                        result.extend([TextNode(text, TextType.TEXT)])
                else:
                    # quoted text
                    result.extend([TextNode(text, text_type)])

    return result
