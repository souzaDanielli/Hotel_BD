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
            INSERT INTO Reserva (data_entrada, data_saida, cpf_cliente, num_quarto)
            VALUES (?, ?, ?, ?) 
        """, (
            reserva.get_data_entrada(),
            reserva.get_data_saida(),
            reserva.get_cpf_cliente(),
            reserva.get_num_quarto()
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
            id, data_entrada, data_saida, cpf_cliente, num_quarto = item

            dados.append({
                "ID": id,
                "Data Entrada": data_entrada,
                "Data Saída": data_saida,
                "CPF Cliente": cpf_cliente,
                "Número do Quarto": num_quarto
            })
        return dados

    except sqlite3.Error as e:
        print(f"Erro ao consultar reservas: {e}")
        return []
    finally:
        conexao.close()

