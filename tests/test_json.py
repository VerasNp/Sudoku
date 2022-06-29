import os
import unittest

from modules.file import get_base_dir
from modules.json import get_json_key_content, get_json_file_content


class TestJsonModule(unittest.TestCase):
    def test_get_json_key_content(self):
        """
        Tests get content from specified key on a json file
        """
        self.assertIsNotNone(get_json_key_content("resources.messages.err.pt_br", "DATA_LINE"))

    def test_get_json_file_content(self):
        """
        Tests get content from json file
        """
        self.assertIsNotNone(get_json_file_content("resources.messages.err.pt_br"))


if __name__ == "__main__":
    unittest.main()
