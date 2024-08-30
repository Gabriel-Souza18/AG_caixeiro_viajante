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

class Grafico_geral:
    def __init__(self, num_geracoes, num_testes):
        self.fitness_geracoes = {}
        self.y = []
        for i in range(0, num_geracoes):
            self.y.append(i)

        self.num_geracoes = num_geracoes
        self.num_testes = num_testes

    def salvar_grafico_geral(self):
        for teste in range(0, self.num_testes):
            r = np.round(np.random.rand(), 1)
            g = np.round(np.random.rand(), 1)
            b = np.round(np.random.rand(), 1)
            plt.plot(self.y, self.fitness_geracoes[teste], marker='.', linestyle='solid', label="teste " + str(teste))
            plt.legend()
        plt.grid(True)
        plt.title(str(self.num_testes) + " Testes")
        plt.xlabel("Geraçoes")
        plt.ylabel("Fitness")
        plt.savefig("Grafico_geral.png")
        plt.close()


class grafico_geracao:
    def __init__(self, fitness):
        self.maximo = []
        self.minimo = []
        self.medio = []
        for i in range(len(fitness)):
            self.maximo.append(fitness[i]["maximo"])
            self.minimo.append(fitness[i]["minimo"])
            self.medio.append(fitness[i]["medio"])
        self.y = list(range(len(fitness)))

    def salvar_grafico_geracao(self):
        plt.plot(self.y, self.maximo, marker='.', linestyle='solid', label="Maximo")
        plt.plot(self.y, self.minimo, marker='.', linestyle='solid', label="Minimo")
        plt.plot(self.y, self.medio, marker='.', linestyle='solid', label="Medio")

        plt.title("Maximos, minimos e médias")
        plt.grid(True)
        plt.xlabel("Geraçoes")
        plt.ylabel("Fitness")
        plt.legend()
        plt.savefig("Grafico_geracao.png")
        plt.close()
