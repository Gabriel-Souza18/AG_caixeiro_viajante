import pickle


class Gravador:
    def __init__(self, matriz: list):
        self.matriz = matriz
        self.caminho_arquivo = "matriz.pkl"

    def gravar(self):
        with open(self.caminho_arquivo, "wb") as arquivo:
            pickle.dump(self.matriz, arquivo)
