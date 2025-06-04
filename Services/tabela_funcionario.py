import sqlite3

DATABASE = "Hotel.db"

conexao = sqlite3.connect(DATABASE)
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS funcionario (
            cpf TEXT NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            data_cadastro DATE NOT NULL
        );
    """
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela FUNCIONÁRIO criada com sucesso!")
