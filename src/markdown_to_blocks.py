def markdown_to_blocks(markdown: str) -> list[str]:
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.strip():
            result.append(block.strip())
    return result
