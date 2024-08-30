import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def mostrar_grafo(grafo: nx.Graph):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    labels = nx.get_edge_attributes(grafo, 'peso')
    nx.draw(grafo, pos, with_labels=True, node_size=500, font_size=10)  # Plota o grafo
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.savefig("grafo.png")
    plt.close()

#    plt.show()  # Exibe o gráfico

class Grafico:
    def __init__(self, num_geracoes, num_testes):
        self.fitness_geracoes = {}
        self.y = []
        for i in range(0, num_geracoes):
            self.y.append(i)

        self.num_geracoes = num_geracoes
        self.num_testes = num_testes

    def show_grafico(self):
        for teste in range(0, self.num_testes):
            r = np.round(np.random.rand(), 1)
            g = np.round(np.random.rand(), 1)
            b = np.round(np.random.rand(), 1)
            plt.plot(self.y, self.fitness_geracoes[teste], marker=' ', linestyle='dashed', label="teste " + str(teste))
            plt.grid(True)
            plt.xlabel("Geraçoes")
            plt.ylabel("Fitness")
            plt.legend()
        plt.savefig("Grafico.png")
        plt.close()