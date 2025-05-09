import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev"})
        print(node)

    def test_eq(self):
        node = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev", "target": "_blank"})
        node2 = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_children(self):
        node = HTMLNode(tag = "a", children=[HTMLNode("b", "pie sucks")], props = {"href": "https://www.dandi.dev"})
        print(node)

if __name__ == "__main__":
    unittest.main()