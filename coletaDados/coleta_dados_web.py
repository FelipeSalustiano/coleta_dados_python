import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

print(extracao.text.strip())

# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('Título: ', titulo)

'''
Desafio)
Filtrar tags ['h2', 'p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag) 
'''
cont_h2 = 0
cont_p = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        cont_h2 += 1
    elif linha_texto.name == 'p':
        cont_p += 1

print(f'Total <h2>: {cont_h2} -- Total <p>: {cont_p}')
    


