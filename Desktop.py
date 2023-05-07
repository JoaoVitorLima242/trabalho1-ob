from Computador import Computador

class Desktop (Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        print(f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: R$ {float(self.preco)}\nPotencia da fonte: {self.potenciaDaFonte}")

    def cadastrar(self):
        print("Aparelho cadastrado com sucesso!")