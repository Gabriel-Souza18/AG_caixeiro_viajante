import networkx as nx
import matplotlib.pyplot as plt


def mostrar_grafo(grafo: nx.Graph):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    labels = nx.get_edge_attributes(grafo, 'peso')
    nx.draw(grafo, pos, with_labels=True, node_size=500, font_size=10)  # Plota o grafo
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.savefig("grafo.png")
#    plt.show()  # Exibe o gráfico
