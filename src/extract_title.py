from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks


def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                if len(block.split(" ")[0]) == 1:
                    return " ".join(block.split(" ")[1:]).strip()
            case _:
                continue

    raise Exception("Error: No H1 heading found")
