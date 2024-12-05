from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, ano, tipo):
        super().__init__(modelo, ano)
        self.tipo: str = tipo
        
    def editar_tipo(self, novo_tipo):
        if novo_tipo and novo_tipo.isalpha():
            self.tipo = novo_tipo
            print("Tipo de moto alterado com sucesso")
        else:
            print("Tipo de moto inválido. O tipo deve conter apenas letras.")
    
    def __str__(self):
        return f'{self.modelo} - {self.ano} - Tipo: {self.tipo}'
