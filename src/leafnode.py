from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self,tag=None,  value = None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == "":
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"