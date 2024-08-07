import unittest

from Utils.Gravador import Gravador
from Utils.Leitor import Leitor
from criador.Criador_grafo import Criador_grafo
from criador.Criador_matriz import Criador_matriz


class MyTestCase(unittest.TestCase):
    def test_criador_matriz(self):
        criador_matriz = Criador_matriz()
        test = criador_matriz.criar_modificar_matriz()
        gravador = Gravador("teste.pkl")
        gravador.gravar(criador_matriz.matriz)
        self.assertEqual(test, 0)  # add assertion here

    def test_criador_grafo(self):
        criador_grafo = Criador_grafo(Leitor("teste.pkl"))
        test = criador_grafo.criar_modificar_grafo()
        self.assertEqual(test, 0)

if __name__ == '__main__':
    unittest.main()
