lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
lista_precos = [100, 50, 1000, 800, 35]
# pegar um item
produto = input("Digite o nome do produto: ")
if produto in lista_produtos:
    posicao = lista_produtos.index(produto)
    preco = lista_precos[posicao]
    print(f"Preço do produto {produto} é R${preco}")
else:
    print(f"Produto {produto} não encontrado na lista: {lista_produtos}")
    
# pegar um valor de item no dicionário
dic_produtos = {"iphone": 100, "ipad": 50, "apple watch": 1000, "airpod": 800, "macbook": 35}
print(f"Preço do item no dicionário: R${dic_produtos['airpod']}")

dic_vendas = {"lira": [1000, 500, 1500], "joao": [500, 400, 500]}
print(f"Vendas do funcionário Jão: {dic_vendas['joao']}")

# adicionar um item ao dicionário
dic_produtos["teste"] = 12000
print(dic_produtos)

#editar um item do dicionário
dic_produtos["apple watch"] = 1
print(dic_produtos)   

# remover um item do dicionário
dic_produtos_removido = dic_produtos.pop("airpod")
print(f"Produto removido {dic_produtos_removido}")
print(dic_produtos)

# verificar se um item existe no dicionário
print("iphone" in dic_produtos)
print("iphone" in dic_produtos.keys())
print(12000 in dic_produtos.values())

# transformar informações em um nova lista
produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)

# contagem de itens no dicionário
qtde = len(dic_produtos)
print(f"{qtde} produto(s)")