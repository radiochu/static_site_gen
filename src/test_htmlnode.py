import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')
        
    def test_props_to_html_with_no_props(self):
        # Test with no properties
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_with_empty_props(self):
        # Test with empty properties dictionary
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_raises_error(self):
        node = HTMLNode()
        # Use assertRaises to check if the method raises the expected error
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_constructor(self):
    # Test with all parameters
        tag = "div"
        value = "content"
        children = [HTMLNode(tag="p", value="child")]
        props = {"class": "container"}
    
        node = HTMLNode(tag=tag, value=value, children=children, props=props)
        
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual

    def test_repr_method(self):
        # Create an HTMLNode with some values
        node = HTMLNode(tag="a", value="click me", props={"href": "https://example.com"})
        # Get the string representation
        repr_string = repr(node)
        # Check if it contains the essential information
        self.assertTrue("a" in repr_string)  # Check if tag is in the string
        self.assertTrue("click me" in repr_string)  # Check if value is in the string
        self.assertTrue("href" in repr_string)  # Check if prop key is in the string
        self.assertTrue("https://example.com" in repr_string)  # Check if prop value is in the string

if __name__ == "__main__":
    unittest.main()