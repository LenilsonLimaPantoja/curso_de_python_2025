import os  # Importa o módulo 'os' para manipular diretórios e arquivos do sistema operacional

# Exibe o diretório atual (onde o script está sendo executado)
print(os.getcwd())

# Lista todos os arquivos e pastas no diretório atual (raiz do projeto)
lista_raiz = os.listdir()
print(f"Arquivos na raiz do projeto {lista_raiz}")

# Lista os arquivos dentro da pasta "arquivos"
lista_pasta_arquivos = os.listdir(path="arquivos")
print(f"Arquivos na pasta arquivo {lista_pasta_arquivos}")

# Percorre todos os arquivos encontrados dentro da pasta "arquivos"
for nome_arquivo in lista_pasta_arquivos:
    # Verifica se o arquivo é um arquivo de texto (contém "txt" no nome)
    if "txt" in nome_arquivo:
        # Se o nome do arquivo contém "22", move o arquivo para a subpasta "22"
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        # Se o nome do arquivo contém "23", move o arquivo para a subpasta "23"
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

# --- PARTE 2: Consumo de API de cotação de moedas ---

import requests  # Importa a biblioteca 'requests' para fazer requisições HTTP

# URL da API pública que retorna a cotação atual de algumas moedas em relação ao real (BRL)
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

# Faz uma requisição GET ao link da API
resposta = requests.get(link)
print(resposta)  # Exibe o status da resposta (ex: <Response [200]>)

# Converte a resposta da API (em formato JSON) para um dicionário Python
dic_resposta = resposta.json()

# Percorre cada moeda retornada no dicionário
for moeda in dic_resposta:
    # Acessa o dicionário com as informações da moeda específica (ex: USD-BRL)
    dic_conversao_moeda = dic_resposta[moeda]
    # Pega o valor atual da cotação (campo 'bid')
    valor_moeda = dic_conversao_moeda["bid"]
    # Exibe o código da moeda e o valor da cotação
    print(moeda, valor_moeda)