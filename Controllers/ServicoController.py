import sqlite3
from Models.Servico import Servico

DATABASE = "Hotel.db"

def conectaBD():
    return sqlite3.connect(DATABASE)

def incluirServico(servico):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO servico (id_funcionario, descricao, id_cliente, id_quarto)
            VALUES (?, ?, ?, ?)
        """, (
            servico.get_id_funcionario(),
            servico.get_descricao(),
            servico.get_id_cliente(),
            servico.get_id_quarto()
        ))
        conexao.commit()
        print("Serviço inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir serviço: {e}")
    finally:
        conexao.close()

def consultarServicos():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT id, id_funcionario, descricao, id_cliente, id_quarto FROM servico')
        rows = cursor.fetchall()
        servicos = []
        for row in rows:
            id, id_funcionario, descricao, id_cliente, id_quarto = row
            servico = Servico(id, id_funcionario, descricao, id_cliente, id_quarto)
            servicos.append(servico)
        return servicos
    except sqlite3.Error as e:
        print(f"Erro ao consultar serviços: {e}")
        return []
    finally:
        conexao.close()

def excluirServico(id):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        # Verifica se o serviço existe
        cursor.execute("SELECT id FROM servico WHERE id = ?", (id,))
        if cursor.fetchone() is None:
            print(f"Serviço com id {id} não encontrado.")
            return False

        cursor.execute("DELETE FROM servico WHERE id = ?", (id,))
        conexao.commit()
        print(f"Serviço com id {id} excluído com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao excluir serviço: {e}")
        return False
    finally:
        conexao.close()

def alterarServico(servico):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE servico
            SET id_funcionario = ?, descricao = ?, id_cliente = ?, id_quarto = ?
            WHERE id = ?
        """, (
            servico.get_id_funcionario(),
            servico.get_descricao(),
            servico.get_id_cliente(),
            servico.get_id_quarto(),
            servico.get_id()
        ))
        conexao.commit()
        print(f"Serviço com id {servico.get_id()} alterado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao alterar serviço: {e}")
        return False
    finally:
       conexao.close()