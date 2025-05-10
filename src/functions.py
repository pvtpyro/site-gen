from textnode import TextType, TextNode


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


