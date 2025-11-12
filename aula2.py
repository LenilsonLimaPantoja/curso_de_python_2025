faturamento = 1000
custo = 600

lucro = faturamento - custo
# texto = "O lucro foi de R$ " + str(lucro) + " e o faturamento foi de R$ " + str(faturamento)
texto = f"O lucro foi de R$ {lucro:.2f} e o faturamento foi de R$ {faturamento:.2f}"

print(texto)

email = " EMAIL_FALSO@gmail.com "

print(f"Email em letras minúsculas: '{email.lower()}'")
print(f"Email sem espaços: '{email.strip()}'")

# tamanho
print(f"Quantidade de caracteres: {len(email)}")

# posição
posicao = email.find("@")
print(f"Posição do '@': {posicao}")

#pedaços de texto
print(f"Posição de 12 a 14: {email[12:14]}") # não inclui a posição 14
print(f"Servidor do email: {email[posicao+1:]}") # servidor do email
print(f"Email: {email[:posicao]}") # email

# trocar pedaço de texto
novo_email = email.replace("gmail.com", "yahoo.com.br", 1)
print(f"Novo email: {novo_email}")

nome = "lenilson lima"
print(f"Nome com a primeira letra maiúscula: {nome.capitalize()}")
print(f"Nome com a primeira letra de cada palavra maiúscula: {nome.title()}")
print(f"Nome com letras maiúsculas: {nome.upper()}")

# formatação númerica
faturamento = 1000000 #número inteiro
custo = 600000 #número inteiro

imposto = 0.15 * faturamento #float

lucro = faturamento - custo - imposto

margem = lucro / faturamento;

mensagem = f"O lucro da loja foi de R$ {lucro:,.2f} e a margem foi de {margem:.2%}" # string
print(mensagem)

# exercicio
nome_ex = "João Paulo Lira"
email_ex = "emailfalsodolira@gmail.com"

# descubra o servidor do email

posicao_arroba_ex = email_ex.find("@")
servidor_email_ex = email_ex[posicao_arroba_ex+1:]
print(f"Servidor do email: {servidor_email_ex}")

#descubra o 1º nome do usuário
posicao_nome_ex = nome_ex.find(" ")
primeiro_nome_ex = nome_ex[:posicao_nome_ex]
print(f"Primeiro nome: {primeiro_nome_ex}")

# criar uma mensagem personalizada dizendo "Usuário 1º nome foi cadastrado com sucesso no email tal"
mensagem_ex = f"Usuário {primeiro_nome_ex} foi cadastrado com sucesso no email {email_ex}"
print(mensagem_ex)