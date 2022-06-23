import unittest

from modules.validators import validate_input


class TestValidator(unittest.TestCase):
    def test_input(self):
        self.assertEqual(validate_input("A, 1:1"),
                         "Formato de dado de entrada errado! Siga o formato <COLUNA>, <LINHA>: <NUMERO> ou <COLUNA>,<LINHA>: <NUMERO>")

        self.assertEqual(validate_input("A,1:1"),
                         "Formato de dado de entrada errado! Siga o formato <COLUNA>, <LINHA>: <NUMERO> ou <COLUNA>,<LINHA>: <NUMERO>")
        self.assertEqual(validate_input("A, 1: 1"), [['COL', 'A'], ['LIN', '1'],
                                                     ['DATA',
                                                      '1']])
        self.assertEqual(validate_input("A,1: 1"), [['COL', 'A'], ['LIN', '1'],
                                                    ['DATA',
                                                     '1']])


if __name__ == "__main__":
    unittest.main()
