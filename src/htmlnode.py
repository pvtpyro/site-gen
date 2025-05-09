class HTMLNode:
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value
        # A list of HTMLNode objects representing the children of this node
        self.children = children
        #A dictionary of key-value pairs representing the attributes of the HTML tag. 
        # For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    def __repr__(self):
        result = f'<{self.tag}'
        if self.props:
            result += self.props_to_html()
        result += '>'

        if self.value:
            result += self.value
        else:
            result += ''.join([f'{child}' for child in self.children])

        result += f'</{self.tag}>'
        return result

        # print(f"{self.tag}, {self.value}, {self.children}, {self.props_to_html()}")

    def __eq__(self, other):
        return (self.tag, self.value, self.children, self.props) == (other.tag, other.value, other.children, other.props)

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = " "
        for key, val in self.props.items():
            string += f'{key}="{val}" '
        return string