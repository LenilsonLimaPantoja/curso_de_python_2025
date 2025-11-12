faturamento = 1100 #número inteiro
custo = 600 #número inteiro

print("Faturamento:", faturamento)
novas_vendas = 1000 #número inteiro

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento #float
print("Imposto:", imposto)

lucro = faturamento - custo - imposto
print("Faturamento + novas vendas:", faturamento)
print("Custo:", custo)
print("Lucro:", lucro)

mensagem = f"O lucro da loja foi de: R$ {lucro:.2f}" # string
print(mensagem)

teve_lucro = False # boolean

margem_lucro = lucro / faturamento
print("Margem:", margem_lucro)

# int = números inteiros
# float = números casa decimal
# strings = textos
# boolean = booleanos (true, false)

# mod -> %
# resto da divisão de um número pelo outro
# 10 % 3

anos = 310 / 12
print(anos ,"anos")

anos = int(310 / 12)
print(anos ,"anos")

#floor division -> //
anos = 310 // 12
print(anos ,"anos")

meses = 310 % 12
print(meses ,"meses")