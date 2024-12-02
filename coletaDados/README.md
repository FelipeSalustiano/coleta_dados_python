# Explicações sobre o arquivo coleta_dados_basico

## Importações
- import requests


Biblioteca utilizada para enviar requisições HTTP, para acessar páginas web 

- from bs4 import BeaultifulSoup

Da biblioteca "bs4" importamos a classe BeaultifulSoup que facilita a análise e a extração de dados de páginas HTML ou XML

## Fazendo a requisição 
### response = requests.get('link do site')

-  **requests.get('link do site')** faz uma requisição HTTP de tipo GET para URL fornecida, ou seja, acessa uma página web 

- **response** é a variavel que vai armazenar a resposta da requisição