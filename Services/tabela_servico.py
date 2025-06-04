import sqlite3

DATABASE = "Hotel.db"

conexao = sqlite3.connect(DATABASE)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS servico (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        id_funcionario TEXT NOT NULL,
        id_cliente TEXT NOT NULL,
        id_quarto TEXT NOT NULL,
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(cpf),
        FOREIGN KEY (id_cliente) REFERENCES Cliente(cpf),
        FOREIGN KEY (id_quarto) REFERENCES Quarto(num_quarto)
    )""")

conexao.commit()
cursor.close()
conexao.close()
print("Tabela SERVICO criada com sucesso!")
