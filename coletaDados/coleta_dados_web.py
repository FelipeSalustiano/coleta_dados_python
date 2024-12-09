import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fazendo a requisição e a extração dos dados 
url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# print(extracao.text.strip())

# -=-=-= Extraindo só os titulos em <h2> no HTML -=-=-=
# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('Título: ', titulo)

# -=-=-= Fazendo a contagem de quantas vezes o <h2> e o <p> aparecem no HTML -=-=-=
# cont_h2 = 0
# cont_p = 0

# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         cont_h2 += 1
#     elif linha_texto.name == 'p':
#         cont_p += 1

# print(f'Total de títulos <h2>: {cont_h2}')
# print(f'Total de parágrafos <p>: {cont_p}')
    
# -=-=-=- Método simplificado -=-=-=-
# cont_h2 = len(extracao.find_all('h2'))
# cont_p = len(extracao.find_all('p'))
# print(f'Total de títulos <h2>: {cont_h2}')
# print(f'Total de parágrafos <p>: {cont_p}')
#     

# -=-=-= Exibindo somente o texto das tags <h2> e <p> -=-=-=
# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print('Título: \n', titulo)
#     elif linha_texto.name == 'p':
#         titulo = linha_texto.text.strip()
#         print('Parágrafo: \n', titulo)

# -=-=-= Exibir tags Aninhada -=-=-=
