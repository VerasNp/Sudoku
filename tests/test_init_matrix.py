import unittest

from modules.matrix import init_matrix


class TestInitMatrix(unittest.TestCase):
    def test_init_matrix(self):
        """
        Testa matriz de inicialização
        """
        self.assertEquals(init_matrix(),
                          [[[None, None, None], [None, None, None], [None, None, None]], [[None, None, None], [None, None, None], [None, None, None]], [[None, None, None], [None, None, None], [None, None, None]]])


if __name__ == "__main__":
    unittest.main()
