from textnode import TextType, TextNode
import re


# TODO check bold and italic
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(old_nodes)
        else:
            sections = node.text.split(delimiter)
            for i, section in enumerate(sections):
                if i % 2 == 0:
                    # even, just text or empty
                    result.append(TextNode(section, TextType.NORMAL))
                else: 
                    # odd, should be md, unless something isn't closed properly
                    result.append(TextNode(section, TextType.CODE))

    return result


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image_daniel(old_nodes):
    for node in old_nodes:
        last_ndx = 0
        for match in re.finditer(r'!\[(.*?)\]\((.*?)\)', node.text):
            if match.start() > last_ndx:
                yield TextNode(node.text[last_ndx:match.start()], TextType.NORMAL)
            yield TextNode(match[1], TextType.IMAGES, match[2])
            last_ndx = match.end()
        if last_ndx < len(node.text):
            yield TextNode(node.text[last_ndx:], TextType.NORMAL)

def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
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
    print("!!!RESULTS", results)
    return results

def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
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
    return results