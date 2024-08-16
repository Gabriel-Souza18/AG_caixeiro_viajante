from .geradores import *


class Populacao:
    def __init__(self, grafo: nx.Graph, npopulacao):
        self.geracoes = []
        self.grafo = grafo
        self.geracao = []
        self.npopulacao = npopulacao

    def geracao_aleatoria(self):
        for cidade in range(0, self.npopulacao):
            self.geracao.append(gerar_individuo_aleatorio(self.grafo))
        self.geracoes.append(self.geracao)

    def geracao_cruzamento(self):
        melhores = self.selecionar_melhores()
        self.geracao = []
        for i in range(0, self.npopulacao):
            individuo1 = random.choice(melhores)
            individuo2 = random.choice(melhores)
            filho = cruzamento(self, individuo1, individuo2)
            self.geracao.append(filho)
        self.geracoes.append(self.geracao)


    def selecionar_melhores(self):
        melhores = []
        for individuo in self.geracao:
            if len(melhores) < 5:
                melhores.append(individuo)
            else:
                for melhor in melhores:
                    if individuo["fitness"] < melhor["fitness"]:
                        melhores.remove(melhor)
                        melhores.append(individuo)
                        break
        return melhores

    def imprimir_geracao(self):
        for individuo in self.geracao:
            print(individuo)

