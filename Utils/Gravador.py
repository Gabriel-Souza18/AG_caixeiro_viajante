import pickle


class Gravador:
    def __init__(self, caminho):
        self.caminho_arquivo = caminho

    def gravar(self, matriz):
        with open(self.caminho_arquivo, "wb") as arquivo:
            pickle.dump(matriz, arquivo)
