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
            INSERT INTO Quarto (num_quarto, descricao, id_reserva)
            VALUES (?, ?, ?) 
        """, (
            quarto.get_num_quarto(),
            quarto.get_descricao(),
            quarto.get_id_reserva()
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
            num_quarto, descricao, id_reserva = item

            dados.append({
                "Número do Quarto": num_quarto,
                "Descrição": descricao,
                "ID da Reserva": id_reserva
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
            SET descricao = ?, id_reserva = ?
            WHERE num_quarto = ?
        """, (
            quarto["Descrição"],
            quarto["ID da Reserva"],
            quarto["Número do Quarto"]
        ))
        conexao.commit()
        print(f"Quarto {quarto['Número do Quarto']} alterado com sucesso!")
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