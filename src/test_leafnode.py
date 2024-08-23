import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode(value='Raw text')
        self.assertEqual(node.to_html(), 'Raw text')

    def test_to_html_with_tag(self):
        node = LeafNode('p', 'This is a paragraph of text.')
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_with_tag_and_props(self):
        node = LeafNode('a', 'Click me!', props={'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode('p')

    def test_to_html_no_children(self):
        node = LeafNode('p', 'Text')
        self.assertEqual(node.children, None)

if __name__ == '__main__':
    unittest.main()
