# entrada é uma matriz de distancias

class Leitor:
    def __init__(self, caminho):
        self.caminho_arquivo = caminho

    def ler_matriz(self):
        with open(self.caminho_arquivo, "r") as arquivo:
            matriz = []
            for linha in arquivo:
                linha_atual = linha.strip().split("  ")
                linha_atual = [int(x) for x in linha_atual if x != ""]
                linha = []
                matriz.append(linha_atual)
        return matriz

