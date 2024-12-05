from carro import Carro
from moto import Moto

class LojaDeVeiculos:
    def __init__(self, nome):
        self.nome : str = nome
        self.estoque : list = []
    
    def adicionar_carro(self, modelo, ano):
        carro_obj = Carro(modelo=modelo, ano=ano)
        self.estoque.append(carro_obj)
        print('Carro adicionado com sucesso!')
        
    def adicionar_moto(self, modelo, ano, tipo):
        moto_obj = Moto(modelo=modelo, ano=ano, tipo=tipo)
        self.estoque.append(moto_obj)
        print('Moto adicionado com sucesso!')

    def listar_veiculos(self):
        if len(self.estoque) == 0:
            print('NENHUM CARRO NO ESTOQUE')
            return
            
        for veiculo in self.estoque:
            print(f'\n{veiculo}')
            
    def buscar_veiculo_por_modelo(self, modelo):
        carro_encontrado = None
        
        for veiculo in self.estoque:
            if veiculo.modelo == modelo:
                carro_encontrado = veiculo
                
        return carro_encontrado

    def remover_veiculo(self, veiculo):
        self.estoque.remove(veiculo)
        print('Veiculo removido com sucesso')


