import sqlite3
from Models.Quarto import Quarto

# Conectando ao banco de dados
def conectaBD():
    return sqlite3.connect("Hotel.db")

# Incluir Quarto
def incluirQuarto(quarto):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Quarto (num_quarto, descricao)
            VALUES (?, ?) 
        """, (
            quarto.get_num_quarto(),
            quarto.get_descricao(),
        ))
        conexao.commit()
        print("Quarto inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir quarto: {e}")
    finally:
        conexao.close()

# Consultar Quarto
def consultarQuarto():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Quarto")
        lista = cursor.fetchall()

        dados = []
        for item in lista:
            num_quarto, descricao = item

            dados.append({
                "Num_Quarto": num_quarto,
                "Descricao": descricao
            })
        return dados

    except sqlite3.Error as e:
        print(f"Erro ao consultar quartos: {e}")
        return []
    finally:
        conexao.close()

# Alterar Quarto
def alterarQuarto(quarto):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE Quarto
            SET descricao = ?
            WHERE num_quarto = ?
        """, (
            quarto["Descricao"],
            quarto["Num_Quarto"]
        ))
        conexao.commit()
        print(f"Quarto {quarto['Num_Quarto']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar quarto: {e}")
    finally:
        conexao.close()

# Excluir Quarto
def excluirQuarto(num_quarto):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Quarto WHERE num_quarto = ?", (num_quarto,))
        conexao.commit()
        print(f"Quarto {num_quarto} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir quarto: {e}")
    finally:
        conexao.close()