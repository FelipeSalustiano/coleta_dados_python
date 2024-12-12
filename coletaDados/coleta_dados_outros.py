import pymysql 
import pandas as pd
from sqlalchemy import create_engine


# Função para conectar com o banco de dados (mostra os dados em tupla)
def conexao_mysql(host, usuario, senha, banco_dados, tabela): 
    # Criar conexão
    conection = pymysql.connect(host=host, user=usuario, password=senha, db=banco_dados)
    cursor = conection.cursor()

    # Executar consulta
    query = f'''SELECT c.nome as nome_cliente, p.nome as nome_produto, SUM(p.preco) as preco_total
    FROM {tabela} c 
    JOIN pedido pe ON pe.id_cliente = c.id_cliente 
    JOIN produto p ON p.id_produto = pe.id_produto 
    GROUP BY nome_cliente, nome_produto
    ORDER BY preco_total DESC
    LIMIT 10'''
    
    cursor.execute(query)

    # Buscar resultados 
    resultados = cursor.fetchall()

    # Exibir resultados 
    print('Tabela MySQL')
    for linha in resultados:
        print(linha)

    # Fechar conexão
    cursor.close()
    conection.close()


# Função para conectar com o banco de dados (mostra os dados em dataframe com pandas)
def df_conexao_mysql(host, usuario, senha, banco_dados, tabela):
    
    conection = create_engine('mysql+pymysql://' + usuario + ':' + senha + '@' + host + '/' + banco_dados) 

    query = f'''SELECT c.nome as nome_cliente, p.nome as nome_produto, SUM(p.preco) as preco_total
    FROM {tabela} c 
    JOIN pedido pe ON pe.id_cliente = c.id_cliente 
    JOIN produto p ON p.id_produto = pe.id_produto 
    GROUP BY nome_cliente, nome_produto
    ORDER BY preco_total DESC
    LIMIT 10'''
    
    # Executando a consulta e salvando em um dataframe 
    df = pd.read_sql(query, conection)

    print('Tabela mySQL em dataframe: \n', df.head())
    
    # Fechar conexão
    conection.dispose()
    return df


 # Função para ler arquivo EXCEL
def conexao_excel(path):
   
    df= pd.read_excel(path)

    print('Dados EXCEL: \n', df.head())


# Função para ler o arquivo CSV 
def conexao_csv(path):

    df = pd.read_csv(path)

    print('Dados CSV: \n', df.head())


# Função para ler o arquivo JASON
def conexao_jason(path):

     df= pd.read_json(path)

     print('Dados JASON: \n', df.head())

    

conexao_mysql('localhost', 'root', '1522', 'loja_informatica', 'cliente') 

df_tabela = df_conexao_mysql('localhost', 'root', '1522', 'loja_informatica', 'cliente')

df_tabela.to_excel('arquivoTeste.xlsx', index=False) # Muda o dataframe para um arquivo Excel e baixa ele
conexao_excel('arquivoTeste.xlsx')

df_tabela.to_csv('arquivoTeste.csv', index=False) # Muda o dataframe para um arquivo CSV e baixa ele
conexao_csv('arquivoTeste.csv')

df_tabela.to_json('arquivoTeste.json', orient='records' ,index=False) # Muda o dataframe para um arquivo JSON e baixa ele
conexao_jason('arquivoTeste.json')