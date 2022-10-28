import  mysql.connector

# inicia a conexao
conexao = mysql.connector.connect(
    host = 'localhost',  # Dados do servidor
    user = 'root',
    password = '159357',
    database = 'bdtreinamento', # Tabela que deseja utilizar
)

cursor = conexao.cursor()  # Sempre precisa criar um cursor

"""
colocar nesse espeça uma das opções do CRUD 
para dar o comando necessário
"""
nome_produto = "abcd"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' 
cursor.execute(comando)
conexao.commit()   #e ditar o banco de dados

cursor.close() # Sempre precisa fechar o cursor
conexao.close() # Sempre precisa fechar a conexao


#   CREATE 
# nome_produto = "chocolate"
# valor_produto = 15
# comando = f'INSERT INTO vendas (nome_produto, valor_produto) VALUES ("{nome_produto}", "{valor_produto}")'
# cursor.execute(comando)
# conexao.commit()  # e ditar o banco de dados

#   READ 
# comando = f'SELECT * FROM vendas' 
# cursor.execute(comando)
# resultado = cursor.fetchall()  # ler o bando de dados
# print(resultado)

#   UPDATE
# nome_produto = "Toddynho"
# valor_produto = 6
# comando = f'UPDATE vendas SET valor_produto = {valor_produto} WHERE nome_produto = "{nome_produto}"' 
# cursor.execute(comando)
# conexao.commit()   #e ditar o banco de dados

#   DELETE
# nome_produto = "Toddynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' 
# cursor.execute(comando)
# conexao.commit()   #e ditar o banco de dados