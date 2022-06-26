#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 1 - Programa que imprime a quantidade de números
# pares de 100 até 200, incluindo-os.
#
# entrada de dados
valor = int(input("informe um valor: "))
quantidade = 0

# processamento de dados
for i in range(100, 201):
    if i % 2 == 0:
        print(i)
        quantidade += 1
    else:
        continue

# saida de dados
print(f"A quantidade de números pares de 100 até 200 é {quantidade}")
print("fim do programa")
