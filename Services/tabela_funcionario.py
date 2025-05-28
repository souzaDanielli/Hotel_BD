import sqlite3

DATABASE = "Hotel.db"

conexao = sqlite3.connect(DATABASE)
cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS funcionario (
            cpf INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT,
            data_nascimento DATE,
            data_cadastro DATE
        );
    """
)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela FUNCIONÁRIO criada com sucesso!")
