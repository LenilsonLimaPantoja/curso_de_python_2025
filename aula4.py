# Exemplo 1 - Verificando lucro ou prejuízo
print("EXEMPLO 1:")
faturamento = 1000
custo = 1200
lucro = faturamento - custo

# verifica se houve lucro ou prejuízo
if lucro >= 0:
    print(f"Lucro de: R${lucro}")
else:
    print(f"Prejuízo de: R${lucro}")

# --------------------------------------------------------

# Exemplo 2 - Cadastro de produto em uma lista
print("\nEXEMPLO 2:")
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
novo_produto = input("Digite o nome do produto: ")

# verifica se o produto já existe na lista
if novo_produto in lista_produtos:
    print(f"Produto {novo_produto} já existente")
else:
    print(f"Produto {novo_produto} cadastrado com sucesso")
    lista_produtos.append(novo_produto)

# exibe a lista atualizada
print(lista_produtos)

# --------------------------------------------------------

# Exemplo 3 - Cálculo de bônus com estrutura condicional simples
print("\nEXEMPLO 3:")
# Regras:
# - Vendas maiores que 15.000 → bônus de R$500
# - Vendas entre 5.000 e 15.000 → bônus de R$100
# - Vendas menores que 5.000 → sem bônus
vendas = 7000

if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000:
        bonus = 100
    else:
        bonus = 0

print(f"Bônus do funcionário: {bonus}")

# --------------------------------------------------------

# Exemplo 4 - Cálculo de bônus com elif (forma mais limpa)
print("\nEXEMPLO 4:")
vendas2 = 17000

if vendas2 >= 15000:
    bonus = 500
elif vendas2 >= 5000:
    bonus = 100
else:
    bonus = 0

print(f"Bônus do funcionário: {bonus}")

# --------------------------------------------------------

# Exemplo 5 - Cálculo de bônus considerando meta da empresa
print("\nEXEMPLO 5:")
# Regras:
# - Só ganha bônus se as vendas totais da empresa forem maiores que 100.000
# - Vendas do funcionário > 15.000 → bônus de R$500
# - Vendas entre 5.000 e 15.000 → bônus de R$100
# - Vendas menores que 5.000 → sem bônus
vendas_empresa = 200000
meta_empresa = 100000
vendas_funcionario = 16000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0

print(f"Bônus do funcionário (com meta): {bonus}")