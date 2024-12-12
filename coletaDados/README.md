# Explicações sobre o pacote coletaDados

## Importações e Bibliotecas utilizadas
#### ***import requests***
Biblioteca utilizada para enviar requisições HTTP, para acessar páginas web. 


#### ***from bs4 import BeaultifulSoup***
Da biblioteca "bs4" importamos a classe BeaultifulSoup que facilita a análise e a extração de dados de páginas HTML ou XML.

#### ***import pandas***
Utiliza a biblioteca Pandas para achar tabela em uma url.

### **import pymysql**
Importação utilizada para a conexão com o banco de dados MySQL. 

### **from sqlalchemy import create_engine**
Biblioteca mais avançada, que pode usar SQL puro ou ORM para gerenciar dados de forma mais elegante e estruturada.

## O que cada arquivo coleta_dados faz?
### coleta_dados_basica
Nesse arquivo peguei infromações de uma URL, usei ferramentas para analisar o HTML dessa URL e também usei a biblioteca Pandas para achar tabelas na URL. 

### coleta_dados_web
Nesse arquivo, além de reforçar o aprendizado sobre fazer requisições de URL's, também encontrei e manipulei títulos, parágrafos e links no HTML do site requisitado. 

### coleta_dados_api
Nesse aquivo fiz uma API. Criei funções para enviar um arquivo para um site que faz upload desse arquivo, uma foi com API KEY (chave de acesso) que é uma forma mais segura para enviar o documento. Também criei uma função para baixar esse arquivo que foi enviado.

### coleta_dados_outros
Neste arquivo, conectei o código a um banco de dados MySQL e desenvolvi funções que permitem executar consultas SQL e visualizar os resultados diretamente no terminal. Também implementei a leitura de arquivos nos formatos CSV, JSON e Excel, além de funcionalidades para converter os dados de uma tabela em JSON, CSV ou Excel.

### gerar_dados
Nesse arquvio, fiz uma criação de dados fictícios e usei uma função para criar um arquivo CSV a partir desse resgistros fictícios.  