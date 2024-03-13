class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro(modelo='Audi A6 Sedan', cor='preto', ano=2023)
print(vars(meu_carro))