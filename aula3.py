# 🧮 EXEMPLO 1 — Entrada de dados e cálculo simples
print("EXEMPLO 1:")
faturamento = input("Preencha com o faturamento (apenas números): ")
faturamento = faturamento.replace("R$", "").replace(",", ".")  # remove símbolos e vírgulas
custo = input("Preencha com o custo (apenas números): ")

lucro = float(faturamento) - float(custo)  # converte para float e calcula lucro
print(f"Lucro: {lucro}")

# 💰 EXEMPLO 2 — Soma de valores informados pelo usuário
print("\nEXEMPLO 2:")
vendas_dia1 = float(input("Preencha com a venda do dia 1 (apenas números): "))
vendas_dia2 = float(input("Preencha com a venda do dia 2 (apenas números): "))
print(f"Soma vendas dos dias 1 e 2: {vendas_dia1 + vendas_dia2}")

# 📋 EXEMPLO 3 — Operações básicas com listas numéricas
print("\nEXEMPLO 3:")
lista_vendas = [100, 50, 1000, 800, 35]
print(f"Item 1 da lista: {lista_vendas[0]}")         # primeiro item
print(f"Último item da lista: {lista_vendas[-1]}")   # último item
print(f"Tamanho da lista: {len(lista_vendas)}")      # quantidade de itens
print(f"Soma dos itens: {sum(lista_vendas)}")        # soma de todos
print(f"Maior valor: {max(lista_vendas)}")           # maior valor
print(f"Menor valor: {min(lista_vendas)}")           # menor valor
print(f"Média: {sum(lista_vendas) / len(lista_vendas)}")  # média simples

# 🔍 EXEMPLO 4 — Manipulação de listas (busca, edição, remoção)
print("\nEXEMPLO 4:")
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("airpod" in lista_produtos)                    # verifica se item existe
posicao = lista_produtos.index("airpod")             # encontra posição do item
print(f"Posição: {posicao}")

pedaco_lista = lista_produtos[posicao:]              # fatiamento da lista
print(f"Pedaço da lista: {pedaco_lista}")

lista_precos = [5000, 7000, 3000, 1000, 10000]
novo_preco = lista_precos[0] * 1.1                   # aumenta preço em 10%
lista_precos[0] = novo_preco
print(f"Lista com o novo preço: {lista_precos}")

lista_produtos.remove("ipad")                        # remove pelo nome
print(f"Lista sem o item 'ipad': {lista_produtos}")

item_removido = lista_produtos.pop(1)                # remove pela posição
print(f"Item removido: {item_removido}")
print(f"Lista atualizada: {lista_produtos}")

# ➕ EXEMPLO 5 — Inserção, junção e ordenação de listas
print("\nEXEMPLO 5:")
lista_produtos.append("produto adicionado")          # adiciona no final
print(lista_produtos)

lista_produtos2 = ["PC", "air tag", "caixa de som"]
lista_produtos.extend(lista_produtos2)               # adiciona outra lista
print(lista_produtos)

lista_produtos.insert(1, "airpod")                   # insere na posição 1
print(lista_produtos)

print(f"Airpod aparece {lista_produtos.count('airpod')} vez(es)")  # conta ocorrências

lista_produtos.sort(reverse=False)                   # ordena em ordem alfabética
print(f"Lista ordenada: {lista_produtos}")