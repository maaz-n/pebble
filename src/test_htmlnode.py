import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_tag(self):
        node = HTMLNode(None, "hi", [HTMLNode("p", "child_node_1", None, None)], None)
        self.assertEqual(node.tag, None)

    def test_no_value(self):
        node = HTMLNode("a", None, [HTMLNode("p", "child_node_1", None, None)], None)
        self.assertEqual(node.value, None)

    def test_no_children(self):
        node = HTMLNode("h1", "heading", None, None)
        self.assertEqual(node.children, None)

    def test_no_props(self):
        node = HTMLNode("h1", "heading", None, None)
        self.assertEqual(node.props, None)
