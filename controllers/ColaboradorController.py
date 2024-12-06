from Models.ColaboradorModel import Colaborador

class Colaborador_Controller:
    def __init__(self):
        self.ColaboradorModel = Colaborador
    
    @staticmethod
    def logar(cpf, senha):
        resultado = Colaborador.autenticar(cpf, senha)
        if resultado["success"]:
            print(f"Login realizado com sucesso! Cargo: {resultado['cargo']}")
            return resultado["cargo"]
        else:
            print(f"Erro no login: {resultado['message']}")
            return None
    
    def cadastrar_colaborador(self, cpf, nome, cargo, senha):
        
        colaborador = Colaborador(cpf=cpf, nome=nome, cargo=cargo, senha=senha)
        if colaborador.cadastrar():
            print("Colaborador cadastrado com sucesso.")
            return True
        else:
            print("Erro ao cadastrar colaborador. Verifique as informações e tente novamente.")
            return False
    
    def autenticar_colaborador(self, cpf, senha):
        print("\n--- Autenticação de Colaborador ---")
        cpf = input("Digite o CPF (apenas números): ").strip()
        senha = input("Digite a senha: ").strip()

        resultado = Colaborador.autenticar(cpf, senha)

        if resultado["success"]:
            print(f"Autenticação bem-sucedida. Cargo: {resultado['cargo']}.")
            return resultado["cargo"]
        else:
            print(f"Erro na autenticação: {resultado['message']}.")
            return None
        
    @staticmethod
    def listar_colaboradores():
        print("\n--- Lista de Colaboradores ---")
        colaboradores = Colaborador.listar_colaboradores()

        if colaboradores:
            print(f"{'CPF':<15} {'Nome':<20} {'Cargo':<15}")
            print("-" * 50)
            for colaborador in colaboradores:
                print(f"{colaborador[0]:<15} {colaborador[1]:<20} {colaborador[2]:<15}")
        else:
            print("Nenhum colaborador cadastrado.")
    
    def alterar_senha(self, cpf, senha_atual, nova_senha):
        try:
            colaborador = Colaborador()
            sucesso = Colaborador.alterar_senha(cpf, senha_atual, nova_senha)
            if sucesso:
                print("Senha alterada com sucesso!")
                return True
            else:
                print("Erro ao alterar a senha. Verifique os dados fornecidos.")
                return False
        except Exception as e:
            print(f"Erro no controlador ao alterar senha: {e}")
            return False

    
    def excluir_colaborador(self, id):
        print("\n--- Exclusão de Colaborador ---")
        id = input("Digite o Id do colaborador que deseja excluir: ").strip()

        if Colaborador.excluir(id):
            print("Colaborador excluído com sucesso.")
            return True
        else:
            print("Erro ao excluir colaborador. Verifique se o colaborador existe.")