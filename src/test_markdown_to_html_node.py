import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_headings(self):
        md = """
        # This is an H1 heading

        ## This is an H2 heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is an H1 heading</h1><h2>This is an H2 heading</h2></div>",
        )

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
    > This is a
    > blockquote block

    this is paragraph text

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote_complex(self):
        md = """
    > The **first** line of wisdom
    > a second line with _italic_
    > and a third with `code`

    > A separate quote block

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<blockquote>The <b>first</b> line of wisdom a second line with <i>italic</i> and a third with <code>code</code></blockquote>"
            "<blockquote>A separate quote block</blockquote>"
            "</div>",
        )

    def test_ordered_list(self):
        md = """
    1. List item 1
    2. List item 2
    3. List item 3
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>List item 1</li><li>List item 2</li><li>List item 3</li></ol></div>",
        )

    def test_ordered_list_complex(self):
        md = """
    1. First with **bold**
    2. Second with _italic_
    3. Third with `code`

    1. A separate list
    2. With two items

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ol><li>First with <b>bold</b></li><li>Second with <i>italic</i></li><li>Third with <code>code</code></li></ol>"
            "<ol><li>A separate list</li><li>With two items</li></ol>"
            "</div>",
        )

    def test_unordered_list(self):
        md = """
    - List item 1
    - List item 2
    - List item 3
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul></div>",
        )

    def test_unordered_list_complex(self):
        md = """
    - First with **bold**
    - Second with _italic_
    - Third with `code`

    - A separate list
    - With two items

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ul><li>First with <b>bold</b></li><li>Second with <i>italic</i></li><li>Third with <code>code</code></li></ul>"
            "<ul><li>A separate list</li><li>With two items</li></ul>"
            "</div>",
        )

    def test_mixed_blocks(self):
        md = """
    # Heading with **bold**

    > A quote with _italic_
    > and a second line

    - first item with `code`
    - second item

    1. ordered one
    2. ordered two

    Final paragraph
    across two lines
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading with <b>bold</b></h1>"
            "<blockquote>A quote with <i>italic</i> and a second line</blockquote>"
            "<ul><li>first item with <code>code</code></li><li>second item</li></ul>"
            "<ol><li>ordered one</li><li>ordered two</li></ol>"
            "<p>Final paragraph across two lines</p>"
            "</div>",
        )

    def test_unordered_list_with_links(self):
        md = """
        - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
        - [Why Tom Bombadil Was a Mistake](/blog/tom)
        - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ul>"
            '<li><a href="/blog/glorfindel">Why Glorfindel is More Impressive than Legolas</a></li>'
            '<li><a href="/blog/tom">Why Tom Bombadil Was a Mistake</a></li>'
            '<li><a href="/blog/majesty">The Unparalleled Majesty of "The Lord of the Rings"</a></li>'
            "</ul>"
            "</div>",
        )
