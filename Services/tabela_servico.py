import sqlite3

DATABASE = "Hotel.db"

conexao = sqlite3.connect(DATABASE)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS servico (
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        id_funcionario INTEGER NOT NULL,
        id_cliente INTEGER NOT NULL,
        id_quarto INTEGER NOT NULL,
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(cpf),
        FOREIGN KEY (id_cliente) REFERENCES cliente(cpf),
        FOREIGN KEY (id_quarto) REFERENCES quarto(n_quarto)
    )""")

conexao.commit()
cursor.close()
conexao.close()
print("Tabela SERVICO criada com sucesso!")
