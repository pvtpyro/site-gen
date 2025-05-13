from htmlnode import HTMLNode

def main():
    # print(TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev"))
    print(HTMLNode(tag = "a", value="link", props = {"href": "https://www.dandi.dev"}))
    print(HTMLNode(tag = "a", children=[HTMLNode("b", "pie sucks")], props = {"href": "https://www.dandi.dev"}))

main()