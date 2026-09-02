import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_one(self):
        markdown = """
        # Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien
        """
        result = extract_title(markdown)

        self.assertEqual(result, "Tolkien Fan Club")

    def test_two(self):
        markdown = """
        ### Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        # I am in fact a Hobbit in all but size.

        >
        > -- J.R.R. Tolkien
        """
        result = extract_title(markdown)

        self.assertEqual(result, "I am in fact a Hobbit in all but size.")
