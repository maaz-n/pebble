from block_to_block_type import BlockType, block_to_block_type
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                heading_type = "h" + str(len(block.split()[0]))
                heading_text = " ".join(block.split()[1:])
                children = text_to_children(heading_text.strip())
                nodes.append(ParentNode(heading_type, children))

            case BlockType.QUOTE:
                quote = " ".join(
                    [
                        line.replace(">", "").strip()
                        for line in block.split("\n")
                        if line.strip()
                    ]
                )
                children = text_to_children(quote)
                nodes.append(ParentNode("blockquote", children))

            case BlockType.ORDERED_LIST:
                list_items = []
                lines_list = [
                    temp.strip()[3:] for temp in block.split("\n") if temp.strip()
                ]
                for li in lines_list:
                    children = text_to_children(li)
                    list_items.append(ParentNode("li", children))

                nodes.append(ParentNode("ol", list_items))

            case BlockType.UNORDERED_LIST:
                list_items = []
                lines_list = [
                    temp.strip()[2:] for temp in block.split("\n") if temp.strip()
                ]
                for li in lines_list:
                    children = text_to_children(li)
                    list_items.append(ParentNode("li", children))
                nodes.append(ParentNode("ul", list_items))

            case BlockType.CODE:
                result = "\n".join(
                    [
                        section.strip()
                        for section in block.split("\n")
                        if section.strip()
                    ]
                )
                code_content = result.removeprefix("```\n").removesuffix("```")
                code_tag = LeafNode("code", code_content)
                pre_tag = ParentNode("pre", [code_tag])
                nodes.append(pre_tag)

            case BlockType.PARAGRAPH:
                text = " ".join(
                    [
                        section.strip()
                        for section in block.split("\n")
                        if section.strip()
                    ]
                )
                children = text_to_children(text)
                nodes.append(ParentNode("p", children))

    result_node = ParentNode("div", nodes)
    return result_node
