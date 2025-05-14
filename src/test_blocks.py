import unittest
from textnode import BlockType
from blocks import *
from functions import *

class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        heading = """# pie sucks"""
        test:BlockType = block_to_block_type(heading)
        self.assertEqual(
            test,
            BlockType.HEADING
        )

    def test_block_to_block_type_list(self):
        mdlist =  """
- This is a list
- with items
""".strip()
        test:BlockType = block_to_block_type(mdlist)
        self.assertEqual(
            test,
            BlockType.ULIST
        )

    def test_block_to_block_type_olist(self):
        mdlist =  """
1. This is a list
2. with items
""".strip()
        test:BlockType = block_to_block_type(mdlist)
        self.assertEqual(
            test,
            BlockType.OLIST
        )

    def test_block_to_block_type_paragr(self):
        mdlist =  """1.pie REALLY SICLS"""
        test:BlockType = block_to_block_type(mdlist)
        self.assertEqual(
            test,
            BlockType.PARAGRAPH
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


    def test_header_level(self):
        md = """# pie sucks"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>pie sucks</h1></div>",
        )



if __name__ == "__main__":
    unittest.main()