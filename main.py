from criador import *
from Visao import *
from algoritmo_genetico import *


def main():
    num_testes = 5
    num_geracoes = 15
    num_individuos = 20
    chance_mutacao = 5

    arquivo = "lau.txt"  # lau.txt ou sgb.txt

    criador_grafo = Criador_grafo(Leitor(arquivo))
    criador_grafo.criar_grafo()
    grafo = criador_grafo.get_grafo()
    mostrar_grafo(grafo)

    grafico = Grafico_geral(num_geracoes, num_testes)

    populacao = Populacao(grafo, num_individuos, chance_mutacao)

    for teste in range(0, num_testes):
        fitness_teste = []
        estatisticas_fitness = []
        for geracao in range(0, num_geracoes):
            print(f"Geracao {geracao}")
            if geracao == 0:
                populacao.geracao_aleatoria()
            else:
                populacao.geracao_cruzamento()

            populacao.imprimir_geracao()
            fitness_teste.append(fitness_medio(populacao.get_geracao()))
            if teste == num_testes - 1:
                estatisticas_fitness.append(estatisticas_fitness_ind(populacao.get_geracao()))

        grafico.fitness_geracoes[teste] = fitness_teste

        if teste == num_testes - 1:
            grafico_geracao_obj = grafico_geracao(estatisticas_fitness)
            grafico_geracao_obj.salvar_grafico_geracao()
    grafico.salvar_grafico_geral()


if __name__ == "__main__":
    main()