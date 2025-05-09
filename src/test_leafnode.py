import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_plain_text(self):
        node = LeafNode("","Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Hello, world!")
        self.assertEqual(node.to_html(), "<strong>Hello, world!</strong>")

if __name__ == "__main__":
    unittest.main()