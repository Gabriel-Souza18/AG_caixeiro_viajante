import random
import numpy as np
from .geradores import *


class Populacao:
    def __init__(self, grafo: nx.Graph, npopulacao):
        self.geracoes = []
        self.grafo = grafo
        self.geracao = []
        self.npopulacao = npopulacao
        self.pesos_cruzamento = []
        self.chance_mutacao = 5

    def geracao_aleatoria(self):
        self.geracao =[]
        for cidade in range(0, self.npopulacao):
            self.geracao.append(gerar_individuo_aleatorio(self.grafo))
        self.geracoes.append(self.geracao)

    def individuo_aleatorio(self):
        individuo = {}
        caminho = []
        fitness = 0
        raiz = int(random.uniform(0, len(self.grafo.nodes())))
        while True:
            for i in range(len(self.grafo.nodes()) + 1):
                proximo = random.choice(list(self.grafo.nodes()))
                if proximo not in caminho:
                    caminho.append(proximo)
                    raiz = proximo
            if len(caminho) == len(self.grafo.nodes()):
                print("gerou 1 individuo")
                break
        fitness = avaliacao_fitness(caminho, self.grafo)
        individuo = {'caminho': caminho, 'fitness': fitness}
        return individuo

    def geracao_cruzamento(self):
        melhores = []
        melhores = self.selecionar_melhores()
        self.geracao = []
        self.geracao.append(melhores[0])
        for i in range(1, self.npopulacao):
            self.pesos_cruzamento = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            individuo1 = random.choices(melhores, weights=self.pesos_cruzamento, k=1)
            individuo2 = random.choices(melhores, weights=self.pesos_cruzamento, k=1)
            filho = self.cruzamento(individuo1[0], individuo2[0])
            filho["caminho"] = self.mutacao(filho["caminho"])
            self.geracao.append(filho)
        self.geracoes.append(self.geracao)

    def selecionar_melhores(self):
        return sorted(self.geracao, key=lambda individuo: individuo["fitness"])

    def cruzamento(self, individuo1, individuo2):
        filho = {}
        caminho = []
        fitness = 0
        for i in range(len(self.grafo.nodes())):
            if i < len(individuo1["caminho"]) / 2:
                caminho.append(individuo1["caminho"][i])
            else:
                if individuo2["caminho"][i] not in caminho:
                    caminho.append(individuo2["caminho"][i])

        if len(caminho) < len(self.grafo.nodes()):
            for i in range(len(self.grafo.nodes())):
                if individuo2["caminho"][i] not in caminho:
                    caminho.append(individuo2["caminho"][i])
        fitness = avaliacao_fitness(caminho, self.grafo)
        filho = {'caminho': caminho, 'fitness': fitness}
        return filho

    def mutacao(self, caminho: list):
        if random.randrange(start=0, stop=99) < self.chance_mutacao:
            i = random.randrange(start=0, stop=len(self.grafo.nodes())-1)
            while True:
                k = random.randrange(start=0, stop=len(self.grafo.nodes())-1)
                if k != i:
                    break

            auxiliar = caminho[i]
            caminho[i] =caminho[k]
            caminho[k] = auxiliar

        return caminho

    def imprimir_geracao(self):
        for individuo in self.geracao:
            print(individuo)

        print(f"Fitness medio da geracao: {fitness_medio(self.geracao)}")

    def get_geracao(self):
        return self.geracao