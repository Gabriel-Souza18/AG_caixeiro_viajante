from criador import *
from Visao import *
from algoritmo_genetico import *


criador_matriz = Criador_matriz(Gravador("matriz.pkl"))
# criador_matriz.criar_modificar_matriz()
# criador_matriz.print_matriz()

criador_grafo = Criador_grafo(Leitor("matriz.pkl"))
criador_grafo.criar_grafo()
grafo = criador_grafo.get_grafo()

mostrar_grafo(grafo)

gerar_populacao(grafo, 10)


