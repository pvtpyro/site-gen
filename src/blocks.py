from functions import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import BlockType, TextNode, TextType
import re

def markdown_to_blocks(markdown: str):
    blocks: list[str] = []
    split_blocks = markdown.split("\n\n")
    for block in split_blocks:
        if block != "":
            blocks.append(block.strip())
    return blocks

def block_to_block_type(text:str):
    if re.match(r'#{1,6} ', text) and len(text.splitlines()) == 1:
        return BlockType.HEADING
    elif text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    else:
        lines = text.split('\n')
        if all([ line.startswith(">") for line in lines ]):
            return BlockType.QUOTE
        if all([ line.startswith("- ") for line in lines ]):
            return BlockType.ULIST
        
        currentLineNumber = 1
        isOList = True
        for line in lines:
            match = re.search(r"^(\d)\. ", line)
            if not match:
                isOList = False
                break

            if int(match[1]) != currentLineNumber:
                isOList = False
                break

            currentLineNumber += 1
        
        if isOList:
            return BlockType.OLIST
        
        return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children) 

def block_to_html_node(block: str):
    block_type: BlockType = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text:str):
    text_nodes = text_to_textnodes(text)
    children: list[HTMLNode] = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block: str):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children: list[HTMLNode] = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block:str):
    level = 0
    # level = block.count("#")
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block:str):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def olist_to_html_node(block:str):
    items = block.split("\n")
    html_items: list[HTMLNode] = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block:str):
    items = block.split("\n")
    html_items:list[HTMLNode] = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block:str):
    lines = block.split("\n")
    new_lines:list[str] = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)