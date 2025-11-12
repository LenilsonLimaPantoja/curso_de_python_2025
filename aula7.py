# Exemplo 1: cálculo de imposto com base no preço dos produtos
print("Exemplo 1:")

# Lista de preços dos produtos
# produtos até 1000 → 10% de imposto
# produtos acima de 1000 → 15% de imposto
lista_precos = [1500, 1000, 800, 2000]

# Função que retorna a taxa de imposto de acordo com o preço do produto
def calcular_taxa_imposto(preco):
    if preco > 1000:
        taxa = 0.15  # imposto de 15% se o preço for maior que 1000
    else:
        taxa = 0.1   # imposto de 10% caso contrário
    return taxa

# Função que calcula o total de imposto de uma lista de preços
def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa_imposto = calcular_taxa_imposto(preco)  # obtém a taxa de imposto
        imposto = taxa_imposto * preco               # calcula o imposto do produto
        imposto_total += imposto                     # soma ao total
    return imposto_total

# Calcula e exibe o total de imposto da primeira lista
imposto_lista1 = calcular_imposto(lista_precos)
print(f"Total de imposto da lista 1 R${imposto_lista1}")

# Exemplo 2: mesma função aplicada em outra lista de preços
print("\nExemplo 2:")
lista2_precos = [500, 4000, 3200, 2600, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(f"Total de imposto da lista 2 R${imposto_lista2}")

# Exemplo 3: função simples apenas para imprimir mensagens
print("\nExemplo 3:")

# Função que imprime instruções para se inscrever no canal
def se_escreve_no_canal():
    print("Clica no botão abaixo do video onde está escrito se inscreva")
    print("Dê um like no vídeo")

# Chamada da função
se_escreve_no_canal()