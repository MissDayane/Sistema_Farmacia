from utils.menus import menu_colaborador, menu_login, menu_medicamento, menu_cliente,menu_venda

def main():
    print("Bem-vindo ao Sistema de Farmácia!")


    while True:
        print("\n--- Tela de Login ---")
        if menu_login():
            print("\nLogin realizado com sucesso!")
            break
        else:
            print("Falha no login. Tente novamente.")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Menu de Clientes")
        print("2. Menu de Medicamentos")
        print("3. Menu de Vendas")
        print("4. Menu de Colaboradores")
        print("0. Sair do Sistema")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            menu_cliente()
        elif opcao == '2':
            menu_medicamento()
        elif opcao == '3':
            menu_venda()
        elif opcao == '4':
            menu_colaborador()
        elif opcao == '0':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()