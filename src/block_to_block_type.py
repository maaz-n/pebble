import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown: str) -> BlockType:
    # HEADING
    for i in range(1, 7):
        pattern = "#" * i + " "
        if markdown.startswith(pattern):
            return BlockType.HEADING

    # CODE
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE

    # lines = markdown.split("\n")
    lines = [line.strip() for line in markdown.split("\n") if line.strip()]

    # QUOTE
    is_quote = True
    for line in lines:
        if not line.strip().startswith(">"):
            is_quote = False
    if is_quote:
        return BlockType.QUOTE

    # UOL
    is_uol = True
    for line in lines:
        if line and not line.startswith("- "):
            is_uol = False
    if is_uol:
        return BlockType.UNORDERED_LIST

    # OL
    is_ol = True
    for i, line in enumerate(lines, start=1):
        if line and not line.startswith(f"{i}. "):
            is_ol = False
    if is_ol:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
