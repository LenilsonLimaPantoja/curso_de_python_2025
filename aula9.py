import os

print(os.getcwd())

lista_raiz = os.listdir()
print(f"Arquivos na raiz do projeto {lista_raiz}")

lista_pasta_arquivos = os.listdir(path="arquivos")
print(f"Arquivos na pasta arquivo {lista_pasta_arquivos}")

for nome_arquivo in lista_pasta_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")
            
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(link)
print(resposta)
dic_resposta = resposta.json()
# print(dic_resposta)
for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]
    print(moeda, valor_moeda)