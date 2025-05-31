import sqlite3
from Models.Cliente import Cliente

# Conectando ao banco de dados
def conectaBD():
    return sqlite3.connect("Hotel.db")

# Incluindo Reserva
def incluirReserva(reserva):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Reserva (data_entrada, data_saida, cpf_cliente)
            VALUES (?, ?, ?) 
        """, (
            reserva.get_data_entrada(),
            reserva.get_data_saida(),
            reserva.get_cpf_cliente()
        ))
        conexao.commit()
        print("Reserva inserida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir reserva: {e}")
    finally:
        conexao.close()

# Consultar Reserva
def consultarReserva():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Reserva")
        lista = cursor.fetchall()

        dados = []
        for item in lista:
            id, data_entrada, data_saida, cpf_cliente = item

            dados.append({
                "ID": id,
                "Data_Entrada": data_entrada,
                "Data_Saida": data_saida,
                "CPF_Cliente": cpf_cliente
            })
        return dados

    except sqlite3.Error as e:
        print(f"Erro ao consultar reservas: {e}")
        return []
    finally:
        conexao.close()

# Alterar Reserva
def alterarReserva(reserva):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE Reserva
            SET data_entrada = ?, data_saida = ?, cpf_cliente = ?
            WHERE id = ?
        """, (
            reserva["data_entrada"],
            reserva["data_saida"],
            reserva["cpf_cliente"],
            reserva["id"]
        ))
        conexao.commit()
        print(f"Reserva com ID {reserva['id']} alterada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar reserva: {e}")
    finally:
        conexao.close()

# Excluir Reserva
def excluirReserva(id):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Reserva WHERE id = ?", (id,))
        conexao.commit()
        print(f"Reserva com ID {id} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir reserva: {e}")
    finally:
        conexao.close()

