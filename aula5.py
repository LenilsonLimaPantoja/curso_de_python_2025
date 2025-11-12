# Exemplo 1 - Buscar produto em listas paralelas
print("EXEMPLO 1:")
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
lista_precos = [100, 50, 1000, 800, 35]

# solicita o nome do produto ao usuário
produto = input("Digite o nome do produto: ")

# verifica se o produto está na lista e exibe o preço correspondente
if produto in lista_produtos:
    posicao = lista_produtos.index(produto)
    preco = lista_precos[posicao]
    print(f"Preço do produto {produto} é R${preco}")
else:
    print(f"Produto {produto} não encontrado na lista: {lista_produtos}")

# --------------------------------------------------------

# Exemplo 2 - Trabalhando com dicionários (chave -> valor)
print("\nEXEMPLO 2:")
dic_produtos = {
    "iphone": 100,
    "ipad": 50,
    "apple watch": 1000,
    "airpod": 800,
    "macbook": 35
}

# acessando um valor diretamente pela chave
print(f"Preço do item no dicionário: R${dic_produtos['airpod']}")

# --------------------------------------------------------

# Exemplo 3 - Dicionário com listas como valores
print("\nEXEMPLO 3:")
dic_vendas = {
    "lira": [1000, 500, 1500],
    "joao": [500, 400, 500]
}

# acessando as vendas de um funcionário específico
print(f"Vendas do funcionário João: {dic_vendas['joao']}")

# --------------------------------------------------------

# Exemplo 4 - Adicionar um novo item ao dicionário
print("\nEXEMPLO 4:")
dic_produtos["teste"] = 12000
print(dic_produtos)

# --------------------------------------------------------

# Exemplo 5 - Editar o valor de um item existente
print("\nEXEMPLO 5:")
dic_produtos["apple watch"] = 1
print(dic_produtos)

# --------------------------------------------------------

# Exemplo 6 - Remover um item do dicionário
print("\nEXEMPLO 6:")
dic_produtos_removido = dic_produtos.pop("airpod")
print(f"Produto removido: {dic_produtos_removido}")
print(dic_produtos)

# --------------------------------------------------------

# Exemplo 7 - Verificar se um item existe no dicionário
print("\nEXEMPLO 7:")
print("iphone" in dic_produtos)          # verifica se existe a chave "iphone"
print("iphone" in dic_produtos.keys())   # verifica se "iphone" está nas chaves
print(12000 in dic_produtos.values())    # verifica se 12000 está nos valores

# --------------------------------------------------------

# Exemplo 8 - Transformar as chaves e valores do dicionário em listas separadas
print("\nEXEMPLO 8:")
produtos = list(dic_produtos.keys())
print(produtos)

precos = list(dic_produtos.values())
print(precos)

# --------------------------------------------------------

# Exemplo 9 - Contar quantos itens existem no dicionário
print("\nEXEMPLO 9:")
qtde = len(dic_produtos)
print(f"{qtde} produto(s)")