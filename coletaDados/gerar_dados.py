import pandas as pd
import random
from faker import Faker

faker = Faker('pt-BR')

dados_pessoas = []

# Criando todos os registros atravéz do faker e random
for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

# Criando um dicionário com os registros criados 
    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'país': pais
    }
    
    # Armazenando os dados do dicionário na lista "dados_pessoas"
    dados_pessoas.append(pessoa)

# Criando um dataframe da lista informada  
df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

# Essas linhas configuram opções do pandas para exibição de dados no terminal
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.width', None)

print(df_pessoas.to_string())
df_pessoas.to_csv('clientes.csv')

