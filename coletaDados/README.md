# Explicações sobre o pacote coletaDados

## Importações e Bibliotecas utilizadas
#### ***import requests***
Biblioteca utilizada para enviar requisições HTTP, para acessar páginas web 

#### ***from bs4 import BeaultifulSoup***
Da biblioteca "bs4" importamos a classe BeaultifulSoup que facilita a análise e a extração de dados de páginas HTML ou XML

#### ***import pandas***
Utiliza a biblioteca Pandas para achar tabela em uma url 

## O que cada arquivo coleta_dados faz?
### coleta_dados_basica
Nesse arquivo peguei infromações de uma URL, usei ferramentas para analisar o HTML dessa URL e também usei a biblioteca Pandas para achar tabelas na URL 

### coleta_dados_web
Nesse arquivo, além de reforçar o aprendizado sobre fazer requisições de URL's, também encontrei e manipulei títulos, parágrafos e links no HTML do site requisitado 

### coleta_dados_api
Nesse aquivo fiz uma API. Criei funções para enviar um arquivo para um site que faz upload desse arquivo, uma foi com API KEY (chave de acesso) que é uma forma mais segura para enviar o documento. Também criei uma função para baixar esse arquivo que foi enviado.
