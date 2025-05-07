import sqlite3

server = ''
username = ''
password = ''
database = 'Hotel.db'
conexao = sqlite3.connect(database)
print("Banco criado!")