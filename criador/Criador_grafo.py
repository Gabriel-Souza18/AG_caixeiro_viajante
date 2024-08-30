import networkx as nx

from Utils.Leitor import Leitor


class Criador_grafo:
    def __init__(self, leitor: Leitor):
        self.grafo = nx.Graph()
        self.leitor = leitor

    def criar_grafo(self):
        matriz = self.leitor.ler_matriz()
        print(len(matriz))
        for linha in range(0, len(matriz)):
            for coluna in range(0, len(matriz[linha])):
                if linha < coluna and matriz[linha][coluna] is not None:
                    self.grafo.add_edge(linha, coluna, peso=matriz[linha][coluna])

        self.print_grafo()
        return 0

    def print_grafo(self):
        for node in self.grafo.nodes():
            print(f"Vértice {node}:")
            for neighbor, data in self.grafo[node].items():
                peso = data.get("peso", "desconhecido")
                if peso != 0:
                    print(f"  -> Vizinho {neighbor} (peso: {peso})")
                else:
                    print(f"  -> Vizinho {neighbor} : nao tem caminho")

    def get_grafo(self):
        return self.grafo
