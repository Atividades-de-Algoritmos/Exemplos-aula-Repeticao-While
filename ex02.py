#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 2 -programa para contar a quantidade de números
# pares entre dois números quaisquer?
#
# usando o laço While:
num1 = int(input('Entre com o valor inicial: ')) # ler o valor e armazenar em uma variável valor1
num2 = int(input('Entre com o valor final: '))
# num1 = 1
# num2 = 20
contadorPares = 1 # criar uma variável para armazenar a quantidade de números pares entre os valores informados pelo usuário

while num1 <= num2: # criar um laço para contar a quantidade de números pares entre os valores informados pelo usuário
  # print(num1) # imprimir o número informado pelo usuário na tela
  if num1 % 2 == 0: # se o resto da divisão do número informado pelo usuário por 2 for igual a 0
    contadorPares = contadorPares + 1 # incrementar a quantidade de números pares informados pelo usuário
  num1 = num1 + 1   # ficar atento a identação do bloco para evitar um loop infinito
print(contadorPares) # imprimir a quantidade de números pares entre os valores informados pelo usuário
print('fim do programa')





# usando o laço FOR:
# entrada de dados
valor1 = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor1
valor2 = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor2
quantidade = 0 # criar uma variável para armazenar a quantidade de números pares

# processamento de dados
for i in range(valor1, valor2 + 1): # criar um laço para calcular a quantidade de números pares entre os valores informados pelo usuário
    if i % 2 == 0: # se o resto da divisão do número informado pelo usuário por 2 for igual a 0
        print(i) # imprimir o número informado pelo usuário
        quantidade += 1 # incrementar a quantidade de números pares informados pelo usuário
    else: # se o resto da divisão do número informado pelo usuário por 2 não for igual a 0 (número impar)
        continue # continuar o laço de repetição

# saida de dados
print(f"A quantidade de números pares entre {valor1} e {valor2} é {quantidade}") # imprimir a quantidade de números pares entre os valores informados pelo usuário
print("fim do programa")
