from enum import Enum

class TextType(Enum):
    NORMAL = 0
    BOLD = 1
    ITALIC = 2
    CODE = 3
    LINKS = 4
    IMAGES = 5

class TextNode:

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
