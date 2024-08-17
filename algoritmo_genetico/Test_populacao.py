import unittest
import networkx as nx
from algoritmo_genetico.Populacao import Populacao, gerar_individuo_aleatorio, avaliacao_fitness


class TestPopulacao(unittest.TestCase):

    def setUp(self):
        self.grafo = nx.complete_graph(5)
        self.populacao = Populacao(self.grafo, 10)

    def test_selecionar_melhores_ordenacao_por_fitness(self):
        self.populacao.geracao = [
            {'caminho': [0, 1, 2, 3, 4], 'fitness': 10},
            {'caminho': [0, 2, 1, 3, 4], 'fitness': 5},
            {'caminho': [0, 3, 2, 1, 4], 'fitness': 8}
        ]
        melhores = self.populacao.selecionar_melhores()
        self.assertEqual(melhores[0]['fitness'], 5)
        self.assertEqual(melhores[1]['fitness'], 8)
        self.assertEqual(melhores[2]['fitness'], 10)

    def test_geracao_aleatoria_cria_geracao_com_tamanho_correto(self):
        self.populacao.geracao_aleatoria()
        self.assertEqual(len(self.populacao.geracao), 10)

    def test_individuo_aleatorio_gera_individuo_valido(self):
        individuo = self.populacao.individuo_aleatorio()
        self.assertEqual(len(individuo['caminho']), len(self.grafo.nodes()))
        self.assertIn('fitness', individuo)

    def test_geracao_cruzamento_gera_nova_geracao(self):
        self.populacao.geracao_aleatoria()
        self.populacao.geracao_cruzamento()
        self.assertEqual(len(self.populacao.geracao), 10)

    def test_mutacao_altera_caminho_com_chance(self):
        caminho = [0, 1, 2, 3, 4]
        self.populacao.chance_mutacao = 100
        novo_caminho = self.populacao.mutacao(caminho)
        self.assertNotEqual(caminho, novo_caminho)

    def test_mutacao_nao_altera_caminho_sem_chance(self):
        caminho = [0, 1, 2, 3, 4]
        self.populacao.chance_mutacao = 0
        novo_caminho = self.populacao.mutacao(caminho)
        self.assertEqual(caminho, novo_caminho)


if __name__ == '__main__':
    unittest.main()
