#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 3 - Programa que imprime a soma de todos os
# números pares entre dois números quaisquer,
# incluindo-os.
#
# entrada de dados
valor1 = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor1
valor2 = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor2
soma = 0 # criar uma variável para armazenar a soma dos números pares

# processamento de dados
for i in range(valor1, valor2 + 1): # criar um laço para calcular a soma dos números pares entre os valores informados pelo usuário
    if i % 2 == 0: # se o resto da divisão do número informado pelo usuário por 2 for igual a 0
        print(i) # imprimir o número informado pelo usuário
        soma += i # incrementar a soma dos números pares informados pelo usuário
    else: # se o resto da divisão do número informado pelo usuário por 2 não for igual a 0 (número impar)
        continue # continuar o laço de repetição

# saida de dados
print(f"A soma dos números pares entre {valor1} e {valor2} é {soma}") # imprimir a soma dos números pares entre os valores informados pelo usuário
print("fim do programa")
