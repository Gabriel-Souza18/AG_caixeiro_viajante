from criador import *
from Visao import *
from algoritmo_genetico import *


def main():
    num_testes = 10
    num_geracoes = 15
    num_individuos = 10

    arquivo = "sgb.txt"  # lau.txt ou sgb.txt

    criador_grafo = Criador_grafo(Leitor(arquivo))
    criador_grafo.criar_grafo()
    grafo = criador_grafo.get_grafo()
    mostrar_grafo(grafo)

    grafico = Grafico(num_geracoes, num_testes)

    populacao = Populacao(grafo, 10)

    for teste in range(0, num_testes):
        fitness_teste = []
        for geracao in range(0, num_geracoes):
            print(f"Geracao {geracao}")
            if geracao == 0:
                populacao.geracao_aleatoria()
            else:
                populacao.geracao_cruzamento()
            populacao.imprimir_geracao()
            fitness_teste.append(fitness_medio(populacao.get_geracao()))
        grafico.fitness_geracoes[teste] = fitness_teste

    grafico.show_grafico()


if __name__ == "__main__":
    main()