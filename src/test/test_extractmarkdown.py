import unittest
from src.inline_utils import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                           ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_output)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to benz dev](https://www.benz.dev) and [to youtube](https://www.youtube.com/@benzdotdev)"
        expected_output = [("to benz dev", "https://www.benz.dev"), 
                           ("to youtube", "https://www.youtube.com/@benzdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_output)

    def test_extract_markdown_images_no_images(self):
        text = "This text has no images."
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links_no_links(self):
        text = "This text has no links."
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_images_malformed(self):
        text = "This is a broken image ![broken image](not a url"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links_malformed(self):
        text = "This is a broken link [broken link]not a url)"
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
