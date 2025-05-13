from enum import Enum

class TextType(Enum):
    NORMAL = 'normal text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINKS = 'link'
    IMAGES = 'image'

class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object):
        if isinstance(other, TextNode):
            return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
   