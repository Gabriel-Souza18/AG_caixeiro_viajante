import pickle


class Gravador:
    def __init__(self):
        self.caminho_arquivo = "matriz.pkl"

    def gravar(self, matriz):
        with open(self.caminho_arquivo, "wb") as arquivo:
            pickle.dump(matriz, arquivo)
