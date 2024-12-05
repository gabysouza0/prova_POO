from loja import LojaDeVeiculos

def mostrar_menu():
    print("Selecione uma opção:")
    print("1 - Listar veículos")
    print("2 - Adicionar carro")
    print("3 - Adicionar moto")
    print("4 - Buscar veículo por modelo")
    print("5 - Remover veículo")
    print("6 - Sair")

def main():
    loja = LojaDeVeiculos("Loja Central")

    while True:
        mostrar_menu()

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            loja.listar_veiculos()

        elif opcao == "2":
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))
            loja.adicionar_carro(modelo, ano)
            print(f"Carro {modelo} {ano} adicionado com sucesso!")

        elif opcao == "3":
            modelo = input("Digite o modelo da moto: ")
            ano = int(input("Digite o ano da moto: "))
            tipo = input("Digite o tipo da moto (ex: esportiva, custom, etc.): ")
            loja.adicionar_moto(modelo, ano, tipo)
            print(f"Moto {modelo} {ano} adicionada com sucesso!")

        elif opcao == "4":
            modelo = input("Digite o modelo do veículo para buscar: ")
            veiculo = loja.buscar_veiculo_por_modelo(modelo)
            if veiculo:
                print(f"Veículo encontrado: {veiculo}")
            else:
                print("Veículo não encontrado.")

        elif opcao == "5":
            modelo = input("Digite o modelo do veículo a ser removido: ")
            veiculo = loja.buscar_veiculo_por_modelo(modelo)
            if veiculo:
                loja.remover_veiculo(veiculo)
                print(f"Veículo {modelo} removido com sucesso!")
            else:
                print("Veículo não encontrado.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
