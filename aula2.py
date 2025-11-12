# Exemplo 1 - Cálculo de lucro e uso de f-strings
print("Exemplo 1:")
faturamento = 1000  # número inteiro
custo = 600  # número inteiro

# cálculo do lucro
lucro = faturamento - custo

# uso de f-string com formatação de casas decimais
# {:.2f} = número com 2 casas decimais
texto = f"O lucro foi de R$ {lucro:.2f} e o faturamento foi de R$ {faturamento:.2f}"

print(texto)


# Exemplo 2 - Manipulação de textos (strings)
print("\nExemplo 2:")
email = " EMAIL_FALSO@gmail.com "  # string com espaços

# transformar em minúsculas
print(f"Email em letras minúsculas: '{email.lower()}'")

# remover espaços no início e no final
print(f"Email sem espaços: '{email.strip()}'")

# contar quantidade de caracteres
print(f"Quantidade de caracteres: {len(email)}")

# encontrar posição de um caractere
posicao = email.find("@")
print(f"Posição do '@': {posicao}")

# fatiar (pegar pedaços de texto)
print(f"Posição de 12 a 14: {email[12:14]}")  # pega posições 12 e 13 (não inclui a 14)
print(f"Servidor do email: {email[posicao+1:]}")  # parte depois do '@'
print(f"Email: {email[:posicao]}")  # parte antes do '@'

# substituir parte do texto
novo_email = email.replace("gmail.com", "yahoo.com.br", 1)
print(f"Novo email: {novo_email}")


# Exemplo 3 - Formatação de nomes
print("\nExemplo 3:")
nome = "lenilson lima"  # string com nome em minúsculas

# primeira letra maiúscula
print(f"Nome com a primeira letra maiúscula: {nome.capitalize()}")

# primeira letra de cada palavra maiúscula
print(f"Nome com a primeira letra de cada palavra maiúscula: {nome.title()}")

# todas as letras maiúsculas
print(f"Nome com letras maiúsculas: {nome.upper()}")


# Exemplo 4 - Formatação numérica e percentual
print("\nExemplo 4:")
faturamento = 1000000  # número inteiro
custo = 600000  # número inteiro

# cálculo do imposto (15% do faturamento)
imposto = 0.15 * faturamento  # float

# cálculo do lucro
lucro = faturamento - custo - imposto

# cálculo da margem de lucro
margem = lucro / faturamento

# f-string com formatação numérica
# {lucro:,.2f} = separa milhar por vírgula e usa 2 casas decimais
# {margem:.2%} = formata como percentual com 2 casas decimais
mensagem = f"O lucro da loja foi de R$ {lucro:,.2f} e a margem foi de {margem:.2%}"
print(mensagem)


# Exemplo 5 - Exercício prático com strings
print("\nExemplo 5:")
nome_ex = "João Paulo Lira"
email_ex = "emailfalsodolira@gmail.com"

# descobrir o servidor do email
posicao_arroba_ex = email_ex.find("@")
servidor_email_ex = email_ex[posicao_arroba_ex+1:]
print(f"Servidor do email: {servidor_email_ex}")

# descobrir o primeiro nome
posicao_nome_ex = nome_ex.find(" ")
primeiro_nome_ex = nome_ex[:posicao_nome_ex]
print(f"Primeiro nome: {primeiro_nome_ex}")

# criar mensagem personalizada
mensagem_ex = f"Usuário {primeiro_nome_ex} foi cadastrado com sucesso no email {email_ex}"
print(mensagem_ex)