from typing import List, override

from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[LeafNode], props=None) -> None:
        super().__init__(tag, None, children, props)

    @override
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Node must have a tag.")

        if not self.children:
            raise ValueError("Parent Node must have children.")

        result = ""

        for child in self.children:
            result += child.to_html()

        result = f"<{self.tag}>{result}</{self.tag}>"
        return result
