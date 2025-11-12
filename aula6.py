print("Exemplo 1:")
for i in range(3):
    print(f"Teste {i}")
    
lista_precos = [100, 50, 10000, 800, 35]
taxa_imposto = 0.1

for preco in lista_precos:
    imposto = preco * taxa_imposto
    print(f"Preço do produto R${preco}, imposto de R${imposto}")
    
# produtos de até 1000 pagam 10%
# produto acima de 1000 pagam 15%
print("\nExemplo 2:")
for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco;
    print(f"Preço do produto R${preco}, imposto de R${imposto}")
    
# mesma regra de imposto mas eu quero conseguir calcular o total de imposto somado de todos os produtos
print("\nExemplo 3:")
total_imposto = 0

for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco;
    total_imposto = total_imposto + imposto
    
    print(f"Preço do produto R${preco}, imposto de R${imposto}")
print(f"Total de imposto R${total_imposto}")

# calculo percentual de crescimento
# 16000 / 15000 - 1 -> qnts % eu cresci de um ano para o outro
print("\nExemplo 4:")
vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f"No mês de {mes} o crescimento foi de {crescimento:.2%}")
