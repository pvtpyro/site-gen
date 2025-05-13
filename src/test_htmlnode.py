import unittest
from htmlnode import HTMLNode
from functions import *
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    # def test_props(self):
        # node = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev"})
        # print(node)

    def test_eq(self):
        node = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev", "target": "_blank"})
        node2 = HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev", "target": "_blank"})
        self.assertEqual(node, node2)

    # def test_children(self):
        # node = HTMLNode(tag = "a", children=[HTMLNode("b", "pie sucks")], props = {"href": "https://www.dandi.dev"})
        # print(node)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        sample = extract_markdown_images(text)
        should_be = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(sample, should_be) 

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        sample = extract_markdown_links(text)
        should_be = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(sample, should_be) 

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link to an image [image](https://i.imgur.com/zjjcJKZ.png) and another link [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link to an image ", TextType.NORMAL),
                TextNode("image", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another link ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.LINKS, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES,
                    "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()