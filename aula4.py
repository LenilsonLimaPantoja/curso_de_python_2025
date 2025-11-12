faturamento = 1000
custo = 1200
lucro = faturamento - custo

if lucro >= 0:
    print(f"Lucro de: R${lucro}")
else:
    print(f"Prejuízo de: R${lucro}")
    
lista_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
novo_produto = input("Digite o nome do produto: ")

if novo_produto in lista_produtos:
    print(f"Produto {novo_produto} já existente")
else:
    print(f"Produto {novo_produto} cadastrado com sucesso")
    lista_produtos.append(novo_produto)
    
print(lista_produtos)
    
# bonus dos funcionários
# vendas maiores do que 15000, então ele ganha 500 de bonus
# vendas entre 5000 e 15000, então ele ganha 100 de bonus
# vendas menores do que 5000, então ele não ganha bonus
vendas = 7000
if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000:
        bonus = 100
    else:
        bonus = 0
print(f"Bonus do funcionário: {bonus}")

vendas2 = 17000

if vendas2 >= 15000:
    bonus = 500
elif vendas2 >= 5000:
    bonus = 100
else:
    bonus = 0
print(f"Bonus do funcionário: {bonus}")

# bonus dos funcionários
# vendas maiores do que 15000, então ele ganha 500 de bonus
# vendas entre 5000 e 15000, então ele ganha 100 de bonus
# vendas menores do que 5000, então ele não ganha bonus
# so ganha nonus se as vendas totais da empre forem maiores do que 100000
vendas_empresa = 200000
meta_empresa = 100000
vendas_funcionario = 16000

if vendas_funcionario >= 15000 and  vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0
print(f"Bonus do funcionário (com meta): {bonus}")