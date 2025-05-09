import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2) 
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.dandi.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.dandi.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("I am a test", TextType.BOLD)
        node2 = TextNode("I am a test", TextType.CODE)
        self.assertNotEqual(node, node2) 

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://www.dandi.dev")
        node2 = TextNode("This is a text node", TextType.LINKS, "http://www.dandi.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()