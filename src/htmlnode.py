class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return "".join([f' {key}="{value}"' for key, value in (self.props or {}).items()])
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if props == None:
            props = {}
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        if props == None:
            props = {}
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode tag cannot be None")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"     

