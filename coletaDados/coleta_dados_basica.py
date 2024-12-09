import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

print('response: ')
response = requests.get('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(response.text[:1000])

print('soup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:500])

print('pandas: ')
url_teste = pd.read_html ('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')
print(url_teste[2].head(10))