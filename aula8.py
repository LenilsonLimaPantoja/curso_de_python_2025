print("Exemplo 1:")
# Cálculo de bônus baseado em vendas
# Bônus 1: R$2 por venda feita
# Bônus 2: 1% do valor total das vendas

# Função que recebe uma lista de vendas e retorna dois bônus
def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)           # R$2 por cada venda (quantidade de itens)
    bonus2 = 0.01 * sum(lista_vendas)        # 1% do valor total das vendas
    return bonus1, bonus2                    # retorna uma tupla com os dois bônus

# Lista com valores de vendas realizadas
vendas = [100, 250, 400, 1000]

# "Unpacking" da tupla retornada pela função — cada valor é atribuído a uma variável
bonus1, bonus2 = calcular_bonus(vendas)

# Exibe os resultados
print(f"Bonus 1: R$ {bonus1}")
print(f"Bonus 2: R$ {bonus2}")

print("\nExemplo 2:")
# Exemplo de desempacotamento de tuplas dentro de um loop
lista_telas = [(1090, 1080), (2140, 1080)]
for altura, largura in lista_telas:
    print(f"Altura: {altura}px e Largura: {largura}px")

print("\nExemplo 4:")
# Dicionário com vendas de vários vendedores (lista de valores vendidos)
vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# Cria um dicionário para armazenar o bônus de cada funcionário
bonus = {}

# Percorre todos os vendedores e calcula os bônus
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    bonus[vendedor] = [bonus1, bonus2]  # Armazena os dois bônus numa lista
print(f"Bonus de cada funcionário: {bonus}")

# Função que calcula o total de bônus pagos (somando todos os vendedores)
def calcular_total_bonus(bonus):
    total_bonus1 = 0
    total_bonus2 = 0
    for vendedor in bonus:
        total_bonus1 += bonus[vendedor][0]  # Soma dos bônus 1
        total_bonus2 += bonus[vendedor][1]  # Soma dos bônus 2
    return total_bonus1, total_bonus2

# Calcula o total geral de bônus pagos
bonus1, bonus2 = calcular_total_bonus(bonus)
print(f"Total de bonus 1: R${bonus1}")
print(f"Total de bonus 2: R${bonus2}")
print(f"Total de bonus geral: R${bonus1 + bonus2}")