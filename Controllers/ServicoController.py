import sqlite3
from Models.Servico import Servico

DATABASE = "Hotel.db"

def conectaBD():
    conexao = sqlite3.connect(DATABASE)
    return conexao

def incluirServico(servico):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO servico (id, id_funcionario, descricao, id_cliente, id_quarto)
            VALUES (?, ?, ?, ?, ?)
        """, (
            servico.get_id(),
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
        cursor.execute('SELECT * FROM servico')
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
        cursor.execute("DELETE FROM servico WHERE id = ?", (id,))
        conexao.commit()
        print(f"Serviço com id {id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir serviço: {e}")
    finally:
        if conexao:
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
    except sqlite3.Error as e:
        print(f"Erro ao alterar serviço: {e}")
    finally:
        if conexao:
            conexao.close()
