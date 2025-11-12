faturamento = input("Preencha com o faturamento (apena números): ")
faturamento = faturamento.replace("R$", "").replace(",", ".")

custo = input("Preencha com o custo (apena números): ")

lucro = float(faturamento) - float(custo)
print(f"Lucro: {lucro}")

vendas_dia1 = float(input("Preencha com a venda do dia 1 (apena números): "))
vendas_dia2 = float(input("Preencha com a venda do dia 2 (apena números): "))
print(f"Soma vendas dos dias 1 e 2: {vendas_dia1 + vendas_dia2}")

lista_vendas = [100, 50, 1000, 800, 35]

print(f"Item 1 da lista: {lista_vendas[0]}") # pegar item 1 da lista
print(f"Ultimo item da lista: {lista_vendas[-1]}") # pegar ultimo item da lista
print(f"Tamanho da lista: {len(lista_vendas)}") # tamanho da lista
print(f"Soma dos itens da lista: {sum(lista_vendas)}") # soma dos itens da lista
print(f"Maior valor na lista: {max(lista_vendas)}") # valor maximo dos itens da lista
print(f"Menor valor na lista: {min(lista_vendas)}") # valor minimo dos itens da lista
print(f"Média dos itens da lista: {sum(lista_vendas) / len(lista_vendas)}") # media dos itens da lista

# encontrar um elemento (a posição do elemento)
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("airpod" in lista_produtos) # se existe na lista

posicao = lista_produtos.index('airpod');
print(f"Posição: {posicao}")

pedaco_lista = lista_produtos[posicao:]
print(f"Pedaço da lista: {pedaco_lista}")


# editar um item
lista_precos = [5000, 7000, 3000, 1000, 10000]
novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(f"Lista com o novo preço: {lista_precos}")

# remover um item da lista
lista_produtos.remove('ipad') # remove passando o item da lista
print(f"Lista sem o item ipad: {lista_produtos}")

item_removido = lista_produtos.pop(1) # remove passando a posição do item da lista (posso armazenar o item removido)
print(f"Item removido: {item_removido}")
print(f"Lista sem o item {item_removido}: {lista_produtos}")

# adicionar um item na lista
lista_produtos.append("produto adicionado") # adiciona no final da lista
print(lista_produtos)

# adicionar todos os itens de uma lista em outra lista
lista_produtos2 = ["PC", "air tag", "caixa de som"]
lista_produtos.extend(lista_produtos2)
print(lista_produtos)

# inserir um item em uma posição específica
lista_produtos.insert(1, "airpod")
print(lista_produtos)

# quantas vezes um item aparece em uma lista
print(f"Airpod aparece {lista_produtos.count('airpod')} vez(es) na lista")

# ordenar lista 
lista_produtos.sort(reverse=False)
print(f"Lista de produtos ordenada: {lista_produtos}")