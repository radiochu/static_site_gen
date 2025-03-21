import unittest

from textnode import TextNode, TextTypes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        node2 = TextNode("This is a text node", TextTypes.BOLD)
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = TextNode("Text node test", TextTypes.BOLD)
        node2 = TextNode("Text goes here", TextTypes.CODE)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()