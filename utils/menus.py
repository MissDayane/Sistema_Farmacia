from controllers.ColaboradorController import Colaborador_Controller
from controllers.MedicamentoController import medicamento_controller
from controllers.ClienteController import cliente_controller
from controllers.VendaController import venda_controller
import pwinput

def menu_login():
    controller = Colaborador_Controller()
    print("\n--- Tela de Login ---")

    while True:
        print("\n1. Fazer Login")
        print("2. Cadastrar Novo Colaborador")
        print("0. Encerrar Sistema")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cpf = input("Digite o CPF: ").strip()
            senha = pwinput.pwinput("Digite a senha: ", mask="*").strip()

            try:
                cargo = controller.logar(cpf, senha)
                if cargo:
                    print(f"Bem-vindo(a), {cargo}!")
                    return True
                else:
                    print("Falha no login. Verifique suas credenciais e tente novamente.")
            except Exception as e:
                print(f"Erro durante o login: {e}")

        elif opcao == '2':
            print("\n--- Cadastro de Novo Colaborador ---")
            cpf = input("Digite o CPF do novo colaborador: ").strip()
            nome = input("Digite o nome do novo colaborador: ").strip()
            cargo = input("Digite o cargo (Gerente, Vendedor ou Farmacêutico): ").strip()
            senha = pwinput.pwinput("Digite a senha para o novo colaborador: ", mask="*").strip()

            try:
                sucesso = controller.cadastrar_colaborador(cpf, nome, cargo, senha)
                if sucesso:
                    print("Colaborador cadastrado com sucesso!")
                else:
                    print("Erro ao cadastrar colaborador. Verifique os dados.")
            except Exception as e:
                print(f"Erro durante o cadastro: {e}")

        elif opcao == '0':
            print("Encerrando o sistema. Até logo!")
            return None
            exit()

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def menu_colaborador():
    controller = Colaborador_Controller()
    while True:
        print("\n--- Menu de Colaboradores ---")
        print("1. Listar Todos os Colaboradores")
        print("2. Alterar Senha")
        print("3. Excluir Colaborador")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == '1':
                print("\n--- Lista de Colaboradores ---")
                controller.listar_colaboradores()
            elif opcao == '2':
                print("\n--- Alteração de Senha ---")
                cpf = input("Digite o CPF do colaborador: ").strip()
                senha_atual = pwinput.pwinput("Digite a senha atual: ", mask="*").strip()
                nova_senha = input("Digite a nova senha: ").strip()

                sucesso = controller.alterar_senha(cpf, senha_atual, nova_senha)
                if sucesso:
                    print("Senha alterada com sucesso!")
                else:
                    print("Erro ao alterar a senha. Verifique os dados e tente novamente.")
            elif opcao == '3':
                print("\n--- Exclusão de Colaborador ---")
                id = input("Digite o Id do colaborador a ser excluído: ").strip()
                confirmacao = input("Tem certeza? (S/N): ").strip().lower()
                if confirmacao == 's':
                    sucesso = controller.excluir_colaborador(id)
                    if sucesso:
                        print("Colaborador excluído com sucesso!")
                    else:
                        print("Erro ao excluir ALGO")
                else:
                    print("Operação cancelada.")
            elif opcao == '0':
                print("Voltando para o Menu Principal")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except Exception as e:
            print(f"Erro: {e}")

def menu_medicamento():
    controller = medicamento_controller()

    while True:
        print("\n--- Menu de Colaboradores ---")
        print("1. Cadastrar Novo Medicamento")
        print("2. Listar Todos Medicamentos")
        print("3. Buscar Por Medicamento")
        print("4. Atualizar Estoque")
        print("5. Atualizar Preço")
        print("6. Deletar Medicamento")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == '1':
                print("\n--- Cadastrar Novo Medicamento ---")
                nome = input("Digite o nome do Medicamento: ")
                categoria = input("Qual a Categoria do Medimento? ")
                preco = float(input("Digite do Preco do Medicamento(unidade): "))
                estoque = int(input("Digite a Quantidade do Medicamento no Estoque: "))

                try:
                    preco = float(preco.strip().replace(',', '.'))
                    estoque = int(estoque.strip())
                except ValueError:
                    print("Erro: Preço deve ser um número decimal e estoque um número inteiro.")
                    continue

                sucesso = controller.cadastrar_medicamento(nome, categoria, preco, estoque)
                if sucesso:
                    print("Medicamento cadastrado com sucesso!")
                else:
                    print("Erro ao cadastrar medicamento.")

            elif opcao == '2':
                print("\n--- Listar Medicamentos ---")
                controller.listar_medicamentos()
            elif opcao == '3':
                print("\n--- Buscar Por Medicamento ---")
                nome = input("Digite o nome do Medicamento que deseja Consultar: ")
                controller.buscar_medicamento(nome)
            elif opcao == '4':
                print("\n--- Atualizar Estoque ---")
                nome = input("Digite o nome do Medicamento para atualizar o estoque: ").strip()
                quantidade = input("Digite a nova quantidade no estoque: ").strip()
                try:
                    quantidade = int(quantidade)
                except ValueError:
                    print("Erro: A quantidade deve ser um número inteiro.")
                    continue
                sucesso = controller.atualizar_estoque(nome, quantidade)
                if sucesso:
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Erro ao atualizar estoque.")
            elif opcao == '5':
                print("\n-- Atualizar Preço ---")
                nome = input("Digite o nome do Medicamento: ")
                preco = float(input("Digite Novo Preco do Medicamento(unidade): "))
                sucesso = controller.atualizar_preco(nome, preco)
                if sucesso:
                    print("Preço atualizado com sucesso!")
                else:
                    print("Erro ao atualizar preço.")
            elif opcao == '6':
                print("\n--- Deletar Medicamento ---")
                id_medicamento = int(input("Digite o identificador Único do Medicamento a ser deletado: "))
                controller.deletar_medicamento(id_medicamento)
            elif opcao == '0':
                print("Saindo do Menu de Medicamentos...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except Exception as e:
            print(f"Erro: {e}")

def menu_cliente():
    controller = cliente_controller()
    while True:
        print("\n--- Menu Clientes ---")
        print("1. Cadastrar Novo Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente (Nome)")
        print("4. Atualizar Telefone de Cliente")
        print("5. Deletar Cliente")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()
        try:
            if opcao == '1':
                print("\n--- Cadastrar Cliente ---")
                nome = input("Digite o nome do Cliente: ").strip()
                cpf = input("Digite o CPF do Cliente: ").strip()
                telefone = input("Digite telefone do cliente: ").strip()

                if controller.criar_cliente(nome, cpf, telefone):
                    print("Cliente cadastrado com sucesso!")
                else:
                    print("Erro ao cadastrar cliente.")
            
            elif opcao == '2':
                print("\n--- Listar Clientes ---")
                controller.listar_clientes()
            
            elif opcao == '3':
                print("\n--- Buscar Cliente ---")
                nome = input("Digite o nome do cliente para buscar: ").strip()
                controller.buscar_cliente(nome)
            
            elif opcao == '4':
                print("\n--- Atualizar Telefone de Cliente ---")
                cpf = input("Digite o CPF do Cliente: ").strip()
                telefone = input("Digite o novo número de telefone: ").strip()
                if controller.atualizar_telefone(cpf, telefone):
                    print("Telefone atualizado com sucesso!")
                else:
                    print("Erro ao atualizar telefone. Verifique o CPF.")
            
            elif opcao == '5':
                print("\n--- Deletar Cliente ---")
                cpf = input("Digite o CPF do Cliente: ").strip()
                if controller.deletar_cliente(cpf):
                    print("Cliente deletado com sucesso!")
                else:
                    print("Erro ao deletar cliente. Verifique o CPF.")
            
            elif opcao == '0':
                print("Voltando ao Menu Principal...")
                break
            
            else:
                print("Opção inválida. Escolha uma opção válida.")
        except Exception as e:
            print(f"Erro: {e}")

def menu_venda():
    controller = venda_controller()

    while True:
        print("\n--- Menu de Vendas ---")
        print("1. Registrar Nova Venda")
        print("2. Listar Todas as Vendas")
        print("3. Buscar Venda por ID")
        print("4. Histórico de Compras de um Cliente")
        print("5. Histórico de Vendas de um Colaborador")
        print("6. Atualizar Quantidade de Itens")
        print("7. Atualizar Preço de Itens")
        print("8. Deletar Venda")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == '1':
                print("\n--- Registrar Nova Venda ---")
                cpf_cliente = input("Digite o CPF do Cliente: ").strip()
                id_colaborador = int(input("Digite o ID do Colaborador: ").strip())

                itens = []
                while True:
                    print("\nAdicionando Item à Venda:")
                    nome_medicamento = input("Digite o Nome do Medicamento: ").strip()
                    quantidade = int(input("Digite a Quantidade: ").strip())

                    itens.append({
                        "nome_medicamento": nome_medicamento,
                        "quantidade": quantidade,
                    })

                    adicionar_mais = input("Deseja adicionar mais itens? (S/N): ").strip().lower()
                    if adicionar_mais != 's':
                        break

                id_venda = controller.registrar_venda(cpf_cliente, id_colaborador, itens)
                if id_venda:
                    print(f"Venda registrada com sucesso! ID da Venda: {id_venda}")
                else:
                    print("Erro ao registrar venda.")

            elif opcao == '2':
                print("\n--- Listar Todas as Vendas ---")
                controller.listar_vendas()

            elif opcao == '3':
                print("\n--- Buscar Venda por ID ---")
                id_venda = int(input("Digite o ID da Venda: ").strip())
                controller.buscar_venda(id_venda)

            elif opcao == '4':
                print("\n--- Histórico de Compras de um Cliente ---")
                cpf_cliente = input("Digite o CPF do Cliente: ").strip()
                controller.historico_compras_cliente(cpf_cliente)

            elif opcao == '5': 
                print("\n--- Histórico de Vendas de um Colaborador ---")
                id_colaborador = int(input("Digite o ID do Colaborador: ").strip())
                controller.historico_vendas_colaborador(id_colaborador)

            elif opcao == '6':
                print("\n--- Atualizar Quantidade de Itens ---")
                id_item_venda = int(input("Digite o ID do Item da Venda: ").strip())
                nova_quantidade = int(input("Digite a Nova Quantidade: ").strip())
                sucesso = controller.atualizar_quantidade_itens(id_item_venda, nova_quantidade)
                if sucesso:
                    print("Quantidade atualizada com sucesso!")
                else:
                    print("Erro ao atualizar quantidade do item.")

            elif opcao == '7':
                print("\n--- Atualizar Preço de Itens ---")
                id_item_venda = int(input("Digite o ID do Item da Venda: ").strip())
                novo_preco_unitario = float(input("Digite o Novo Preço Unitário: ").strip().replace(',', '.'))
                sucesso = controller.atualizar_preco_itens(id_item_venda, novo_preco_unitario)
                if sucesso:
                    print("Preço atualizado com sucesso!")
                else:
                    print("Erro ao atualizar preço do item.")

            elif opcao == '8':
                print("\n--- Deletar Venda ---")
                id_venda = int(input("Digite o ID da Venda a ser deletada: ").strip())
                confirmacao = input("Tem certeza que deseja deletar esta venda? (S/N): ").strip().lower()
                if confirmacao == 's':
                    sucesso = controller.deletar_venda(id_venda)
                    if sucesso:
                        print("Venda deletada com sucesso!")
                    else:
                        print("Erro ao deletar venda.")
                else:
                    print("Operação cancelada.")

            elif opcao == '0':
                print("Voltando ao Menu Principal...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        except Exception as e:
            print(f"Erro durante a operação: {e}")

        