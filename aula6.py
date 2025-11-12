# Exemplo 1 - Estrutura básica de repetição com range()
print("Exemplo 1:")
for i in range(3):  # repete o bloco 3 vezes (valores: 0, 1, 2)
    print(f"Teste {i}")

# --------------------------------------------------------

# Exemplo 2 - Cálculo de imposto com taxa fixa
print("\nExemplo 2:")
lista_precos = [100, 50, 10000, 800, 35]
taxa_imposto = 0.1  # 10%

# percorre cada item da lista e calcula o imposto
for preco in lista_precos:
    imposto = preco * taxa_imposto
    print(f"Preço do produto R${preco}, imposto de R${imposto}")

# --------------------------------------------------------

# Exemplo 3 - Cálculo de imposto com taxa variável
# produtos até 1000 → 10% de imposto
# produtos acima de 1000 → 15% de imposto
print("\nExemplo 3:")
for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco
    print(f"Preço do produto R${preco}, imposto de R${imposto}")

# --------------------------------------------------------

# Exemplo 4 - Soma total dos impostos cobrados
# mesma regra do exemplo anterior, mas agora somando o total
print("\nExemplo 4:")
total_imposto = 0  # acumulador

for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco
    total_imposto += imposto  # soma o imposto de cada produto

    print(f"Preço do produto R${preco}, imposto de R${imposto}")

# mostra o total final
print(f"Total de imposto R${total_imposto}")

# --------------------------------------------------------

# Exemplo 5 - Cálculo percentual de crescimento entre anos
# fórmula: (valor_atual / valor_anterior - 1)
print("\nExemplo 5:")
print("\nExemplo 4:")
vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}

# percorre os meses do dicionário de 2024 e compara com 2023
for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f"No mês de {mes} o crescimento foi de {crescimento:.2%}")