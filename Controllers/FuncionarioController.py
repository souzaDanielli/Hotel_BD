import sqlite3
from Models.Funcionario import Funcionario

DATABASE = "Hotel.db"

def conectaBD():
    conexao = sqlite3.connect(DATABASE)
    return conexao

def incluirFuncionario(funcionario):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO funcionario (cpf, nome, telefone, data_nascimento, data_cadastro)
            VALUES (?, ?, ?, ?, ?)
        """, (
            funcionario.get_cpf(),
            funcionario.get_nome(),
            funcionario.get_telefone(),
            funcionario.get_data_nascimento(),
            funcionario.get_data_cadastro()
        ))
        conexao.commit()
        print("Funcionário inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir funcionário: {e}")
    finally:
        conexao.close()

def consultarFuncionarios():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM funcionario')
        rows = cursor.fetchall()

        funcionarios = []
        for row in rows:
            cpf, nome, telefone, data_nascimento, data_cadastro = row
            funcionario = Funcionario(cpf, nome, telefone, data_nascimento, data_cadastro)
            funcionarios.append(funcionario)
        return funcionarios
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionários: {e}")
        return []
    finally:
        conexao.close()

def excluirFuncionario(cpf):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM funcionario WHERE cpf = ?", (cpf,))
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Funcionário com CPF {cpf} excluído com sucesso!")
            return True
        else:
            print(f"Nenhum funcionário encontrado com o CPF {cpf}.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao excluir funcionário: {e}")
        return False
    finally:
        conexao.close()

def alterarFuncionario(funcionario):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE funcionario
            SET nome = ?, telefone = ?, data_nascimento = ?, data_cadastro = ?
            WHERE cpf = ?
        """, (
            funcionario.get_nome(),
            funcionario.get_telefone(),
            funcionario.get_data_nascimento(),
            funcionario.get_data_cadastro(),
            funcionario.get_cpf()
        ))
        conexao.commit()
        print(f"Funcionário com CPF {funcionario.get_cpf()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar funcionário: {e}")
    finally:
        conexao.close()


def buscarFuncionarioCpf(cpf):
    conexao = sqlite3.connect("Hotel.db")
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM funcionario WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        return resultado is not None
    except sqlite3.Error as e:
        print(f"Erro ao verificar funcionário: {e}")
        return False
    finally:
        conexao.close()
