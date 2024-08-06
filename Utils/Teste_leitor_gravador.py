import unittest

from Utils.Gravador import Gravador
from Utils.Leitor import Leitor


class MyTestCase(unittest.TestCase):
    def test_leitor_gravador(self):
        matriz1 = [[2, 2, 3], [1, 5, 6], [2, 1, 0]]
        gravador = Gravador()
        gravador.gravar(matriz1)

        leitor = Leitor()
        matriz2 = leitor.ler_matriz()

        self.assertEqual(matriz1, matriz2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
