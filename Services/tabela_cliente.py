import sqlite3

conexao = sqlite3.connect("Hotel.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE Cliente(
                cpf TEXT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                cidade TEXT,
                telefone TEXT NOT NULL
        );
    '''
)
conexao.commit()
cursor.close()
conexao.close()
print("Tabela Cliente criada (ou já existia)!")