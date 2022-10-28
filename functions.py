import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',  # Dados do servidor
    user = 'root',
    password = '159357',
    database = 'bdtreinamento', # Tabela que deseja utilizar
)

cursor = conexao.cursor()

nome_produto = "abacaxi"
valor_produto = values = 0

def cadastrar(produto,valor) -> str and int:  # Cadastra um produto e preço no banco de dados.
    cursor = conexao.cursor()
    nome_produto = str(values['nome_produto'])
    valor_produto = float(values['valor_produto'])
    comando = f'INSERT INTO vendas (nome_produto, valor_produto) VALUES ("{nome_produto}", "{valor_produto}")'
    cursor.execute(comando)
    conexao.commit() 
    conexao.close() # Sempre precisa fechar a conexao
    cursor.close() # Sempre precisa fechar o cursor 
    return produto and valor

def mostrar():   # Mostra o  índice, produto e preço respectivamente.
    comando = f'SELECT * FROM vendas' 
    cursor.execute(comando)
    resultado = cursor.fetchall() 
    print(resultado)

def editar(): # Edita o valor do produto.
    comando = f'UPDATE vendas SET valor_produto = {valor_produto} WHERE nome_produto = "{nome_produto}"' 
    cursor.execute(comando)
    conexao.commit() 

def deletar(): # Deleta um produto pelo nome.
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' 
    cursor.execute(comando)
    conexao.commit()
conexao.close() # Sempre precisa fechar a conexao
cursor.close() # Sempre precisa fechar o cursor