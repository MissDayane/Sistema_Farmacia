import bcrypt
from config.database import criar_conexao, fechar_conexao
import re

class Colaborador:

    def __init__(self, cpf=None, nome=None, cargo=None, senha=None):
       
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo
        self.senha = senha
        self.conn = criar_conexao()
    
    def cadastrar(self):
        
        try:
            conn = criar_conexao()
            with conn.cursor() as cursor:
                senha_hash = bcrypt.hashpw(self.senha.encode('utf-8'), bcrypt.gensalt())
                sql = 'INSERT INTO Colaboradores (CPF_colaborador, nome, cargo, senha) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql, (self.cpf, self.nome, self.cargo, senha_hash))
                conn.commit()
                print("Colaborador cadastrado com sucesso.")
                return True
        except Exception as e:
            print(f"Erro ao cadastrar colaborador: {e}")
            return False
        finally:
            cursor.close()
            fechar_conexao(conn)
    
    @staticmethod
    def autenticar(cpf, senha):
        conn = criar_conexao()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT senha, cargo FROM Colaboradores WHERE CPF_colaborador = %s"
                cursor.execute(sql, (cpf,))
                result = cursor.fetchone()

                if result:
                    senha_hash, cargo = result

                    if isinstance(senha_hash, memoryview):
                        senha_hash = senha_hash.tobytes()

                    if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
                        return {"success": True, "cargo": cargo}
                    else:
                        return {"success": False, "message": "Senha incorreta"}
                else:
                    return {"success": False, "message": "Colaborador não encontrado"}
        except Exception as e:
            print(f"Erro ao autenticar colaborador: {e}")
            return {"success": False, "message": "Erro no sistema"}
        finally:
            cursor.close()
            fechar_conexao(conn)
    
    def listar_colaboradores():

        conn = criar_conexao()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT ID_colaborador, CPF_colaborador, nome, cargo FROM Colaboradores"
                cursor.execute(sql)
                colaboradores = cursor.fetchall()

                if colaboradores:
                    print("Lista de Colaboradores:")
                    for colaborador in colaboradores:
                        print(f"ID_COLABORADOR: {colaborador[0]}CPF: {colaborador[1]}, Nome: {colaborador[2]}, Cargo: {colaborador[3]}")
                    return colaboradores
                else:
                    print("Nenhum colaborador encontrado.")
                    return None
        except Exception as e:
            print(f"Erro ao listar colaboradores: {e}")
            return None
        finally:
            cursor.close()
            fechar_conexao(conn)
    
    @staticmethod
    def validar_senha(senha):
        
        return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', senha))

    
    def alterar_senha(self, cpf, senha_atual, nova_senha):

        
        try:
            conn = criar_conexao()
            autenticar_resultado = Colaborador.autenticar(cpf, senha_atual)
            if not autenticar_resultado["success"]:
                print(f"Erro: {autenticar_resultado['message']}")
                return False
            
            if not Colaborador.validar_senha(nova_senha)["success"]:
                print("Nova senha inválida! A senha deve ter pelo menos 8 caracteres, incluindo 1 número, 1 letra e 1 caractere especial.")
                return False
            
            with conn.cursor() as cursor:
                senha_hash = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt())
                sql = "UPDATE Colaboradores SET senha = %s WHERE CPF_colaborador = %s"
                cursor.execute(sql, (senha_hash, cpf))
                conn.commit()
                print("Senha alterada com sucesso.")
                return True
        except Exception as e:
            print(f"Erro ao alterar a senha: {e}")
            return False
        finally:
            if conn:
                fechar_conexao(conn)

    
    
    def excluir(ID_colaborador):
        try:
            conn = criar_conexao()
            with conn.cursor() as cursor:
                cursor.execute("SELECT nome FROM Colaboradores WHERE ID_colaborador = %s", (ID_colaborador,))
                colaborador = cursor.fetchone()
                if not colaborador:
                    print("Colaborador não encontrado.")
                    return False
                cursor.execute("Update Vendas set ID_colaborador = NULL WHERE ID_colaborador = %s", (ID_colaborador,))
                cursor.execute("DELETE FROM Colaboradores WHERE ID_colaborador = %s", (ID_colaborador,))
                conn.commit()
                print("Colaborador excluído com sucesso.")
                return True
        except Exception as e:
            print(f"Erro ao excluir colaborador: {e}")
            return False
        finally:
            cursor.close()
            fechar_conexao(conn)