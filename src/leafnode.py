from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag: str | None = None,  value: str | None = None, props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == "" or self.tag == None:
            return self.value
        elif self.tag == 'img':
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>"
        elif self.tag == "a":
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"