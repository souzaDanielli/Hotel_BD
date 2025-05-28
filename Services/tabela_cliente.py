import sqlite3

conexao = sqlite3.connect("Hotel.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE Cliente_novo(
                cpf TEXT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                cidade TEXT,
                telefone TEXT NOT NULL
        );
    '''
)
cursor.close()
conexao.close()
print("Tabela Cliente criada (ou já existia)!")