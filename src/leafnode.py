from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == "":
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"