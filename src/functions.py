from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    result: list[TextNode] = []

    for node in old_nodes:
        # print("!!!type:", text_type, node.text)
        # print(type(node))
        if node.text_type != TextType.NORMAL:
            result.append(node)
        else:
            sections = node.text.split(delimiter)
            for i, section in enumerate(sections):
                if i % 2 == 0:
                    # even, just text or empty
                    result.append(TextNode(section, TextType.NORMAL))
                else: 
                    # odd, should be md, unless something isn't closed properly
                    # check delimiter and send proper type
                    result.append(TextNode(section, text_type))
    return result


def extract_markdown_images(text: str):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image_daniel(old_nodes: list[TextNode]):
    for node in old_nodes:
        last_ndx = 0
        for match in re.finditer(r'!\[(.*?)\]\((.*?)\)', node.text):
            if match.start() > last_ndx:
                yield TextNode(node.text[last_ndx:match.start()], TextType.NORMAL)
            yield TextNode(match[1], TextType.IMAGES, match[2])
            last_ndx = match.end()
        if last_ndx < len(node.text):
            yield TextNode(node.text[last_ndx:], TextType.NORMAL)

def split_nodes_image(old_nodes: list[TextNode]):
    results: list[TextNode] = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            images = extract_markdown_images(node.text)
            if images:
                text = node.text
                for alt, url in images:
                    left, text = text.split(f"![{alt}]({url})", 1)
                    if left:
                        results.append(TextNode(left, TextType.NORMAL))
                    results.append(TextNode(alt, TextType.IMAGES, url))
                if text:
                    results.append(TextNode(text, TextType.NORMAL))
            else:
                results.append(TextNode(node.text, TextType.NORMAL))
        else:
            results.append(node)
    # print("!!!RESULTS", results)
    return results

def split_nodes_link(old_nodes: list[TextNode]):
    results: list[TextNode] = []
    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            links = extract_markdown_links(node.text)
            if links:
                text = node.text
                for link_text, url in links:
                    left, text = text.split(f"[{link_text}]({url})", 1)
                    if left:
                        results.append(TextNode(left, TextType.NORMAL))
                    results.append(TextNode(link_text, TextType.LINKS, url))
                if text:
                    results.append(TextNode(text, TextType.NORMAL))
            else:
                results.append(TextNode(node.text, TextType.NORMAL))
        else:
            results.append(node)
    return results

# This is **text** with an _italic_ word and a `code block` 
# and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) 
# and a [link](https://boot.dev)
def text_to_textnodes(text: str):
    results = [TextNode(text, TextType.NORMAL)]
    results = split_nodes_delimiter(results, "**", TextType.BOLD)
    results = split_nodes_delimiter(results, "_", TextType.ITALIC)
    results = split_nodes_delimiter(results, "*", TextType.ITALIC)
    results = split_nodes_delimiter(results, "`", TextType.CODE)
    results = split_nodes_image(results)
    results = split_nodes_link(results)
    return results