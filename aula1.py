# Exemplo 1 - Cálculos com números e tipos de dados básicos
print("Exemplo 1:")

# variáveis numéricas (inteiros)
faturamento = 1100  # número inteiro
custo = 600  # número inteiro

# exibe o faturamento atual
print("Faturamento:", faturamento)

# nova venda realizada
novas_vendas = 1000  # número inteiro

# atualiza o faturamento somando as novas vendas
faturamento = faturamento + novas_vendas

# calcula o imposto (15% do faturamento)
imposto = 0.15 * faturamento  # número decimal (float)
print("Imposto:", imposto)

# calcula o lucro final (faturamento - custo - imposto)
lucro = faturamento - custo - imposto

# exibe os resultados
print("Faturamento + novas vendas:", faturamento)
print("Custo:", custo)
print("Lucro:", lucro)

# cria uma mensagem formatada com f-string (duas casas decimais)
mensagem = f"O lucro da loja foi de: R$ {lucro:.2f}"  # string
print(mensagem)

# variável booleana (verdadeiro ou falso)
teve_lucro = False  # boolean

# calcula a margem de lucro em relação ao faturamento
margem_lucro = lucro / faturamento
print("Margem:", margem_lucro)

# explicação dos tipos de dados em Python
# int = números inteiros (ex: 10, 500, -3)
# float = números decimais (ex: 10.5, 3.14)
# strings = textos (ex: "Olá", 'Python')
# boolean = verdadeiro (True) ou falso (False)

# operador "mod" -> %
# obtém o resto da divisão de um número pelo outro
# exemplo: 10 % 3 retorna 1 (resto da divisão)
# 10 % 3

# divisão normal -> retorna número decimal
anos = 310 / 12
print(anos, "anos")

# conversão para inteiro -> remove as casas decimais
anos = int(310 / 12)
print(anos, "anos")

# floor division -> //
# divisão inteira (descarta o resto automaticamente)
anos = 310 // 12
print(anos, "anos")

# operador módulo (%) -> retorna o resto da divisão
meses = 310 % 12
print(meses, "meses")