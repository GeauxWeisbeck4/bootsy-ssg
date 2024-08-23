from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        else:
            props = self.props_to_html()
            if props:
                return f"<{self.tag}{props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
