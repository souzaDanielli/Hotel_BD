import sqlite3
from Models.Cliente import Cliente

# Conectando ao banco de dados
def conectaBD():
    return sqlite3.connect("Hotel.db")

# Incluindo Cliente
def incluirCliente(cliente):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO Cliente (cpf, nome, data_nascimento, cidade, telefone)
            VALUES (?, ?, ?, ?, ?) 
        """, (
            cliente.get_cpf(),
            cliente.get_nome(),
            cliente.get_data_nascimento(),
            cliente.get_cidade(),
            cliente.get_telefone()
        ))
        conexao.commit()
        print("Cliente inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        conexao.close()

# Consultando Cliente
def consultarCliente():
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT * FROM Cliente")
        lista = cursor.fetchall()
    
        dados = []
        for item in lista:
            cpf, nome, data_nascimento, cidade, telefone = item
        
        dados.append({
            "CPF": cpf,
            "Nome": nome,
            "Data de nascimento": data_nascimento,
            "Cidade": cidade,
            "Telefone": telefone
        })
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar clientes: {e}")
        return []
    finally:
        conexao.close()

# Atualizando Cliente
def alterarCliente(cliente):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE Cliente
            SET cpf = ?, nome = ?, data_nascimento = ?, cidade = ?, telefone = ? 
            WHERE cpf = ?         
            """,(
                cliente["CPF"],
                cliente["Nome"],
                cliente["Data de nascimento"],
                cliente["Cidade"],
                cliente["Telefone"]
        ))
        conexao.commit()
        print("Cliente com o CPF {cliente['CPF']} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar Cliente: {e}")
    finally:
        conexao.close()

#Excluir Cliente
def excluirCliente(cpf):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM Cliente WHERE cpf = ?", (cpf,))
        conexao.commit()
        print("Cliente com CPF {cpf} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir Cliente: {e}")
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
            reserva["Data Entrada"],
            reserva["Data Saída"],
            reserva["CPF Cliente"],
            reserva["Número do Quarto"],
            reserva["ID"]
        ))
        conexao.commit()
        print(f"Reserva com ID {reserva['ID']} alterada com sucesso!")
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