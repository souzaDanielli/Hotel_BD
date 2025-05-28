import sqlite3

conexao = sqlite3.connect("Hotel.db")
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE Quarto (
            num_quarto INTEGER PRIMARY KEY NOT NULL,
            descricao TEXT NOT NULL,
            id_reserva INTEGER NOT NULL,
            FOREIGN KEY (id_reserva) REFERENCES Reserva(id) 
        );
    """
)

cursor.close()
print("Tabela de Quarto criada! ")