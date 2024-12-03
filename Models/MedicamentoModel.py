import psycopg2
from config.database import criar_conexao, fechar_conexao

class Medicamento:
    @staticmethod
    def cadastrar_medicamento(nome, categoria, preco, estoque):
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = """
                    INSERT INTO Medicamentos (nome, categoria, preco, estoque)
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(query, (nome, categoria, preco, estoque))
                    conn.commit()
                    return True
        except psycopg2.Error as e:
            print(f"Erro ao cadastrar medicamento: {e}")
            return False
        finally:
            fechar_conexao(conn)

    @staticmethod
    def listar_medicamentos():
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = "SELECT * FROM Medicamentos"
                    cursor.execute(query)
                    return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Erro ao listar medicamentos: {e}")
            return []
        finally:
            fechar_conexao(conn)

    @staticmethod
    def buscar_medicamento(nome):
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = "SELECT * FROM Medicamentos WHERE nome ILIKE %s"
                    cursor.execute(query, ('%' + nome + '%',))
                    return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Erro ao buscar medicamento: {e}")
            return []
        finally:
            fechar_conexao(conn)

    @staticmethod
    def atualizar_estoque(nome, quantidade):
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = "UPDATE Medicamentos SET estoque = %s WHERE nome ILIKE %s"
                    cursor.execute(query, (quantidade, nome))
                    conn.commit()
                    return cursor.rowcount > 0
        except psycopg2.Error as e:
            print(f"Erro ao atualizar estoque: {e}")
            return False
        finally:
            fechar_conexao(conn)

    @staticmethod
    def atualizar_preco(nome, preco):
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = "UPDATE Medicamentos SET preco = %s WHERE nome ILIKE %s"
                    cursor.execute(query, (preco, nome))
                    conn.commit()
                    return cursor.rowcount > 0
                    return True
        except psycopg2.Error as e:
            print(f"Erro ao atualizar preço: {e}")
            return False
        finally:
            fechar_conexao(conn)

    @staticmethod
    def deletar_medicamento(id_medicamento):
        try:
            conn = criar_conexao()
            with conn:
                with conn.cursor() as cursor:
                    query = "DELETE FROM Medicamentos WHERE ID_medicamento = %s"
                    cursor.execute(query, (id_medicamento,))
                    conn.commit()
                    return cursor.rowcount > 0
        except psycopg2.Error as e:
            print(f"Erro ao deletar medicamento: {e}")
            return False
        finally:
            fechar_conexao(conn)
