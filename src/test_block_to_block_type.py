import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_invalid_heading(self):
        markdown = "####### This is an invalid heading"
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_invalid_ol(self):
        markdown = "1. foo\n2. bar\n5. twinkie"
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_valid_quote(self):
        markdown = "> Quote 1\n>Quote2\n> Quote3"
        result = block_to_block_type(markdown)
        self.assertEqual(result, BlockType.QUOTE)
