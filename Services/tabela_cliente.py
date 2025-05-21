import sqlite3

conexao = sqlite3.connect("Hotel.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE Cliente(
                cpf INTEGER PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                cidade TEXT,
                telefone TEXT NOT NULL
        );
    '''
)

cursor.close()
print("tabela Cliente criada!")