from time import sleep
from functions import cadastrar, mostrar
from PySimpleGUI import PySimpleGUI as sg
import  mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',  # Dados do servidor
    user = 'root',
    password = '159357',
    database = 'bdtreinamento', # Tabela que deseja utilizar
)

# Layout #
sg.theme('DarkPurple6')
layout = [
    [sg.Text('Cadastro de Produtos')],
    [sg.Text('Nome do Produto:', size=(20, 1)),
     sg.Text('Valor do Produto: R$', size=(18, 1))],
    [sg.Input(key='nome_produto', size=(23, 1)),
     sg.Input(key='valor_produto', size=(20, 1))],
    [sg.Output(size=(43,20))],
    [sg.Button('Cadastrar'), sg.Button('Mostrar dados'),
     sg.Button('Editar Preço'), sg.Button('Deletar')]
]
# Window #
window = sg.Window('Tela de cadastro', layout)
# Events read #
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break

    if events == 'Cadastrar':
        cursor = conexao.cursor()
        nome_produto = str(values['nome_produto'])
        valor_produto = float(values['valor_produto'])
        comando = f'INSERT INTO vendas (nome_produto, valor_produto) VALUES ("{nome_produto}", "{valor_produto}")'
        cursor.execute(comando)
        conexao.commit() 
        cursor.close() # Sempre precisa fechar o cursor
        window['valor_produto'].update('')
        window['nome_produto'].update('')
        print(f'{nome_produto.upper()}: R${valor_produto:.2f}')
        print("Produto cadastrado com Sucesso!")

    if events == 'Mostrar dados':
        cursor = conexao.cursor()
        comando = f'SELECT * FROM vendas' 
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        for item in resultado:
            print(f'Índice{item[0]} ~> {item[1]} -- R${item[2]}'.upper())
        cursor.close() # Sempre precisa fechar o cursor

    if events == 'Editar Preço':
        cursor = conexao.cursor()
        nome_produto = str(values['nome_produto'])
        valor_produto = int(values['valor_produto'])   
        comando = f'UPDATE vendas SET valor_produto = {valor_produto} WHERE nome_produto = "{nome_produto}"' 
        cursor.execute(comando)
        conexao.commit()   #e ditar o banco de dados
        cursor.close() # Sempre precisa fechar o cursor
        window['valor_produto'].update('')
        window['nome_produto'].update('')
        print(f'''Preço de {nome_produto} alterado para: R${valor_produto}''')
   


    if events == 'Deletar':
        cursor = conexao.cursor()  # Sempre precisa criar um cursor
        nome_produto = str(values['nome_produto'])
        comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' 
        cursor.execute(comando)
        conexao.commit()   #e ditar o banco de dados
        cursor.close() # Sempre precisa fechar o cursor
        window['nome_produto'].update('')
        print(f'Produto {nome_produto.upper()} deletado com Sucesso!')
