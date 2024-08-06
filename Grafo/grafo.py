import networkx as nx
class Grafo(nx.Graph):
    def __init__(self, nome):
        super().__init__(nome)

