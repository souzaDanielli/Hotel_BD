import sqlite3

conexao = sqlite3.connect("Hotel.db")
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE Reserva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_entrada DATE NOT NULL,
            data_saida DATE NOT NULL,
            cpf_cliente INTEGER NOT NULL,
            num_quarto INTEGER NOT NULL,
            FOREIGN KEY (cpf_cliente) REFERENCES Cliente(cpf),
            FOREIGN KEY (num_quarto) REFERENCES Quarto(num_quarto) 
        );
    """
)

cursor.close()
print("Tabela de Reserva criada! ")

