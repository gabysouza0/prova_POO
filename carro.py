from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)

    def __str__(self):
        return f'{self.modelo} - {self.ano}'
