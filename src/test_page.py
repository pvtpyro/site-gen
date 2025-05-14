import unittest

from page import extract_title

class TestPage(unittest.TestCase):
    
    def test_extract_title(self):
         md = """
# This is a title for a web page.  

This is a paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
         title = extract_title(md)
         self.assertEqual(
            title,
            "This is a title for a web page."
        )
         
    def test_without_title(self):
        md = """
This is a web page without a title/h1.  

This is a paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        try:
            title = extract_title(md) # type: ignore
        except Exception as e:
            assert str(e) == "No heading level 1 provided"

    def test_with_multiple_title(self):
        md = """
# This is a title for a web page.  
# Another H1??? HOW DARE YOU!
This is a paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
# 3 primary headers in a single page? This is out of control!
- This is a list
- with items
        """
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a title for a web page."
        )