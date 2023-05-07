from Computador import Computador

class Notebook (Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        print(f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: R$ {float(self.preco)}\nTempo de Bateria: {self.tempoDeBateria}")

    def cadastrar(self):
        print("Aparelho cadastrado com sucesso!")
