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


def pesos_cruzamento(num_individuos):
    pesos = []
    for i in range(num_individuos, 0, -1):
        pesos.append(i)
    print(pesos)
    return pesos


def fitness_medio(geracao: list):
    soma = 0
    for individuo in geracao:
        soma += individuo["fitness"]

    return soma / len(geracao)


def estatisticas_fitness_ind(geracao):
    fitness = [individuo["fitness"] for individuo in geracao]

    resultado = {
        "minimo": min(fitness),
        "maximo": max(fitness),
        "medio": sum(fitness) / len(fitness)
    }

    return resultado
