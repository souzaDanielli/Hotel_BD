import sqlite3

conexao = sqlite3.connect("Hotel.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE Reserva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_entrada DATE NOT NULL,
            data_saida DATE NOT NULL,
            cpf_cliente TEXT NOT NULL,
            num_quarto TEXT NOT NULL,
            FOREIGN KEY (num_quarto) REFERENCES Quarto(num_quarto),
            FOREIGN KEY (cpf_cliente) REFERENCES Cliente(cpf)
        );
    """
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela de Reserva criada! ")

