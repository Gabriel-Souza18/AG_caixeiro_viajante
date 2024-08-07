# entrada é uma matriz de distancias
import pickle


class Leitor:
    def __init__(self, caminho):
        self.caminho_arquivo = caminho

    def ler_matriz(self):
        with open(self.caminho_arquivo, "rb") as arquivo:
            matriz = pickle.load(arquivo)
        return matriz

