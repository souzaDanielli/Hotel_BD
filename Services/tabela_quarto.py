import sqlite3

conexao = sqlite3.connect("Hotel.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE Quarto (
            num_quarto TEXT PRIMARY KEY NOT NULL,
            descricao TEXT NOT NULL
        );
    """
)
conexao.commit()
cursor.close()
conexao.close()
print("Tabela de Quarto criada! ")