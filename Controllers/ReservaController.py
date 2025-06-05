import sqlite3
from Models.Cliente import Cliente

# Conectando ao banco de dados
def conectaBD():
    conexao = sqlite3.connect("Hotel.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

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
                "Data_Entrada": data_entrada,
                "Data_Saida": data_saida,
                "CPF_Cliente": cpf_cliente,
                "Num_Quarto": num_quarto
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
            SET data_entrada = ?, data_saida = ?, cpf_cliente = ?, num_quarto = ?
            WHERE id = ?
        """, (
            reserva["data_entrada"],
            reserva["data_saida"],
            reserva["cpf_cliente"],
            reserva["num_quarto"],
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

def buscarReservasPorCpf(cpf):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Reserva WHERE cpf_cliente = ?", (cpf,))
        lista = cursor.fetchall()

        dados = []
        for item in lista:
            id, data_entrada, data_saida, cpf_cliente, num_quarto = item
            dados.append({
                "ID": id,
                "Data_Entrada": data_entrada,
                "Data_Saida": data_saida,
                "CPF_Cliente": cpf_cliente,
                "Num_Quarto": num_quarto
            })
        return dados
    except sqlite3.Error as e:
        print(f"Erro ao buscar reservas: {e}")
        return []
    finally:
        conexao.close()

def buscarReservasCompletas():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            SELECT 
                R.id,
                C.nome AS nome_cliente,
                C.cpf AS cpf_cliente,
                R.data_entrada,
                R.data_saida,
                Q.num_quarto,
                Q.descricao
            FROM Reserva R
            INNER JOIN Cliente C ON R.cpf_cliente = C.cpf
            INNER JOIN Quarto Q ON R.num_quarto = Q.num_quarto;
        """)
        lista = cursor.fetchall()

        dados = []
        for item in lista:
            id, nome_cliente, cpf_cliente, data_entrada, data_saida, num_quarto, descricao = item
            dados.append({
                "ID": id,
                "Nome_Cliente": nome_cliente,
                "CPF_Cliente": cpf_cliente,
                "Data_Entrada": data_entrada,
                "Data_Saida": data_saida,
                "Num_Quarto": num_quarto,
                "Descricao": descricao
            })
        return dados
    except sqlite3.Error as e:
        print(f"Erro ao buscar reservas completas: {e}")
        return []
    finally:
        conexao.close()
