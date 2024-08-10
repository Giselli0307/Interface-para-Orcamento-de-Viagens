## Conectar o view como banco de dados
import sqlite3 as lite

## Criar uma conexão -- Nova base de dados
con = lite.connect("dados.db")

# Inserir quantia 
def inserir_quantia_total(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Quantia (valor) VALUES (?)"
        cur.execute(query, i)

# Ver a tabela quantia
def ver_quantia_total():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Quantia")
        row = cur.fetchall()

        for i in row:
            lista_itens.append(i)

    return lista_itens

# Atualizar quantia 
def atualizar_quantia_total():
    with con:
        cur = con.cursor()
        query = "UPDATE Quantia SET valor=? WHERE id=?"
        cur.execute(query, i)
