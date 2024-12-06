from config.database import criar_conexao, fechar_conexao
import re


def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1
    
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2


def validar_cargo(cpf: str) -> str:
    cpf = ''.join(filter(str.isdigit, cpf))
    try:
        conn = criar_conexao()
        with conn.cursor() as cursor:
            sql = "SELECT cargo FROM Colaboradores WHERE CPF_colaborador = %s"
            cursor.execute(sql, (cpf,))
            result = cursor.fetchone()
            if not result:
                print("Colaborador não encontrado.")
                return None
            return result[0]
    except Exception as e:
        print(f"Erro ao verificar cargo: {e}")
        return None
    finally:
        fechar_conexao(conn)

def cargos_validos():
    return ["Gerente", "Vendedor", "Farmacêutico"]

def validar_nome(nome: str) -> str:
    if len(nome) > 100:
        return None
    if not re.fullmatch(r"[A-Za-zÀ-ÿ\s\-']+", nome):
        return None
    return nome.strip().lower().title()

def validar_telefone(telefone:str) -> bool:
    if not telefone.isdigit():
        return False
    if len(set(telefone)) == 1:
        return False
    
    crescente = ''.join(sorted(telefone)) == telefone
    decrescente = ''.join(sorted(telefone, reverse=True)) == telefone
    if crescente or decrescente:
        return False

    return True

def validar_senha2(senha):
        
        return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', senha))