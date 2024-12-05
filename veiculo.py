class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo: str = modelo
        self.ano: int = ano
        
    def __str__(self):
        return f'{self.modelo} - {self.ano}'
    
    def editar_ano(self, novo_ano):
        if novo_ano and novo_ano > 1800:
            self.ano = novo_ano
            print('Ano alterado com sucesso')
        else:
            print('Este número não é válido')
            
    def editar_modelo(self, modelo):
        if modelo.isalpha() and len(modelo):
            self.modelo = modelo
            print('Modelo alterado com sucesso')
        else:
            print('Este modelo não é valido')
