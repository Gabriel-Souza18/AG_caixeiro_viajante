import networkx as nx
import random


def gerar_individuo_aleatorio(grafo: nx.Graph):
    individuo = {}
    caminho = []
    fitness = 0
    raiz = int(random.uniform(0, len(grafo.nodes())))
    while True:
        for i in range(len(grafo.nodes()) + 1):
            proximo = random.choice(list(grafo.nodes()))
            if proximo not in caminho:
                caminho.append(proximo)
                raiz = proximo
        if len(caminho) == len(grafo.nodes()):
            print("gerou 1 individuo")
            break
    fitness = avaliacao_fitness(caminho, grafo)
    individuo = {'caminho': caminho, 'fitness': fitness}
    return individuo


def avaliacao_fitness(caminho: list, grafo: nx.Graph):
    fitness = 0
    for cidade in range(1, len(caminho)):
        fitness += buscar_distancia(grafo, caminho[cidade], caminho[cidade - 1])
    return fitness


def buscar_distancia(grafo: nx.Graph, origem: int, destino: int):
    try:
        distancia = nx.dijkstra_path_length(grafo, origem, destino, weight='peso')
        return distancia
    except nx.NetworkXNoPath:
        return float('inf')


def cruzamento(self, individuo1, individuo2):
    filho = {}
    caminho = []
    fitness = 0
    for i in range(len(individuo1["caminho"])):
        if i < len(individuo1["caminho"]) / 2:
            caminho.append(individuo1["caminho"][i])
        else:
            caminho.append(individuo2["caminho"][i])
    fitness = avaliacao_fitness(caminho, self.grafo)
    filho = {'caminho': caminho, 'fitness': fitness}
    return filho
# nao pode passar pelo mesmo lugar duas vezes CORRIGIR
