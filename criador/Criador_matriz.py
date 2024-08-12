from Utils import Gravador


class Criador_matriz:
    def __init__(self, gravador: Gravador):
        self.num_vertices = 0
        self.matriz = []
        self.gravador = gravador
class Criador_matriz:
    def __init__(self, gravador: Gravador):
        self.num_vertices = 0
        self.matriz = []
        self.gravador = gravador

    def criar_modificar_matriz(self):
        print("Digite a quantidade de vertices: ")
        self.num_vertices = int(input())
        self.iniciar_matriz()
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i < j:
                    print(f"Digite a distancia direta entre {i} e {j}: (se nao tiver digite 0)")
                    entrada = int(input())
                    if entrada != 0:
                        self.matriz[i][j] = entrada
                        self.matriz[j][i] = entrada
                    else:
                        self.matriz[i][j] = None
                        self.matriz[j][i] = None

        self.gravador.gravar(self.matriz)
        return 0

    def iniciar_matriz(self):
        self.matriz = [[None] * self.num_vertices for _ in range(self.num_vertices)]

    def print_matriz(self):
        for linha in self.matriz:
            print(linha)
