import requests

def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'C:/Users/felipe.moreira/Documents/produtos_informatica_pasta/produtos_informatica.xlsx'
    
    # Enviar arquivo 
    requisicao = requests.post('https://file.io', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()
    
    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado. Link para acesso:", url)
    
    
# Função para baixar o arquivo 
def receber_arquivo(file_url):
    # Receber o arquivo 
    requisicao = requests.get(file_url)
    
    # Salvar o arquivo 
    if requisicao.ok:
        with open('produtos_informatica.xlsx','wb') as file:
            file.write(requisicao.content)
            print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo')
        
# Função para enviar o arquivo porém mais protegido, pois uiliza uma chave de acesso (API KEY) 
def enviar_chave():
    # Caminho do arquivo e chave para upload
    caminho = 'C:/Users/felipe.moreira/Documents/produtos_informatica_pasta/produtos_informatica.xlsx'
    api_key = '7FQCTDG.ERV3TSK-KZEMXMN-MEBW9SF-HSK0WWA' #chave de acesso
    
    requisicao = requests.post(
        'https://file.io', 
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': api_key}
    )
    saida_requisicao = requisicao.json()
    url = saida_requisicao['link']
    print("Arquivo enviado com chave. Link para acesso: ", url)
    
    
    
enviar_chave()
enviar_arquivo()
receber_arquivo() # necessita de um parâmetro (a URL)