#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 4  - Programa que calcule o fatorial de um número.
#
# entrada de dados
valor = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor
fatorial = 1 # criar uma variável para armazenar o fatorial

# processamento de dados
for i in range(1, valor + 1): # criar um laço para calcular o fatorial do número informado pelo usuário
    fatorial *= i # multiplicar o fatorial pelo número informado pelo usuário

# saida de dados
print(f"O fatorial de {valor} é {fatorial}") # imprimir o fatorial do número informado pelo usuário
print("fim do programa")