## Chamar a biblioteca do sqlite
import sqlite3 as lite

## Criar uma conexão -- Nova base de dados
con = lite.connect("dados.db")

# Criar a primeira tabela ------------------------------------------------------------------------------------------
## Quantia Total
with con:
  cur = con.cursor()
  cur.execute("CREATE TABLE Quantia(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL)")

## Tabela de despesa 
with con:
  cur = con.cursor()
  cur.execute("CREATE TABLE Despesas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, descricao TEXT, valor DECIMAL)")