import unittest
from textnode import TextNode, TextType
from functions import *

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
        node = TextNode("This is a text node", TextType.LINK, "https://www.dandi.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "http://www.dandi.dev")
        self.assertNotEqual(node, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        should_be = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode("", TextType.TEXT, None)]
        # print(new_nodes)
        self.assertEqual(new_nodes, should_be)

if __name__ == "__main__":
    unittest.main()