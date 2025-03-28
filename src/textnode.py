from enum import Enum
from htmlnode import LeafNode

class TextTypes(Enum):
    NORMAL = 1
    BOLD = 2
    CODE = 3
    LINKS = 4
    IMAGES = 5
    ITALIC = 6

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextTypes.NORMAL:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextTypes.BOLD:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextTypes.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextTypes.ITALIC:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextTypes.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == TextTypes.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"invalid text type: {text_node.text_type}")