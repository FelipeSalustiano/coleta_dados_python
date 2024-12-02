import requests 
from bs4 import BeautifulSoup 

response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:600])

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
