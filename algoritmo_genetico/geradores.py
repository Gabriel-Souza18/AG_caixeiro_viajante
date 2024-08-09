import networkx as nx
import random


def gerar_individuo(grafo: nx.Graph):
    individuo = []
    caminho = []
    fitness = 0
    raiz = int(random.uniform(0, len(grafo.nodes())))
    while True:
        for i in range(len(grafo.nodes())+1):
            proximo = random.choice(list(grafo.neighbors(raiz)))
            if proximo not in caminho:
                caminho.append(proximo)
                raiz = proximo
        if len(caminho) == len(grafo.nodes()):
            print("gerou 1 individuo")
            break
    fitness = avaliacao_fitness(caminho, grafo)
    individuo.append({'caminho': caminho, 'fitness': fitness})
    return individuo


def avaliacao_fitness(caminho: list, grafo: nx.Graph):
    fitness = 0
    for cidade in range(1, len(caminho)):
        fitness += grafo[caminho[cidade]][caminho[cidade - 1]]['peso']
    return fitness


def gerar_populacao(grafo: nx.Graph, nPopulacao):
    populacao = []
    for cidade in range(0, nPopulacao):
        populacao.append(gerar_individuo(grafo))
    imprimir_populacao(populacao)
    return populacao


def imprimir_populacao(populacao: list):
    for individuo in populacao:
        print(individuo)
