from typing import override

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None = None, value: str | None = None, props=None
    ) -> None:
        super().__init__(tag, value, None, props)

    @override
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf Node must have a value")

        if not self.tag:
            return self.value

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    @override
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
