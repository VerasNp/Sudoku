import unittest

from modules.file import check_ext_list, check_ext, read_file, get_base_dir, file_exists


class TestFileModule(unittest.TestCase):
    """
    Tests with some file module functionalities
    """

    def test_check_ext(self):
        """
        Checks if file exists (string separated by points)
        :return:
        """
        self.assertEqual(check_ext("resources.messages.err.pt_br", "json"), True)

    def test_check_ext_list(self):
        """
        Checks if file exists (list of files)
        :return:
        """
        self.assertEqual(check_ext_list(["/resources/messages/err/pt_br.json"], "json"), True)

    def test_file_exists(self):
        full_path = get_base_dir(True) + "resources.messages.err.pt_br"
        self.assertEqual(file_exists(full_path, "json"), True)

    def test_read_file(self):
        path = get_base_dir() + 'resources/config/app.json'
        self.assertIsNotNone(read_file(path))
