#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 4  - Programa que calcule o fatorial de um número.
#
# usando o laço While:

#Exemplo (fatorial sem recursão):
#https://pt.wikipedia.org/wiki/Fatorial

################   1   #########################
numero = int(input('Digite um número inteiro positivo: '))

fat = 1 # inicializar o fatorial com 1
while numero > 0: # criar um laço para calcular o fatorial do número informado pelo usuário
  fat = fat * numero # multiplicar o fatorial pelo número informado pelo usuário
  numero = numero - 1 # decrementar o número informado pelo usuário
print('O fatorial desse número é ', fat) # imprimir o fatorial do número informado pelo usuário

################   2   ###########################
# se a entrada for ZERO
#entrada
num1 = int(input("informe um número :")) # ler o valor e armazenar em uma variável valor1
temp = num1 # armazenar o valor informado pelo usuário em uma variável temporária
fat = 1 # inicializar o fatorial com 1 para o caso de ser ZERO
#processamento de dados
if num1 == 0 : # se o número informado pelo usuário for ZERO
  pass # não fazer nada
else: # se o número informado pelo usuário não for ZERO
  while (num1 > 0): # criar um laço para calcular o fatorial do número informado pelo usuário
    fat = fat * num1 # multiplicar o fatorial pelo número informado pelo usuário
    num1 = num1 - 1 # decrementar o número informado pelo usuário

#saida
print(f"o fatorial de {temp} é {fat}") # imprimir o fatorial do número informado pelo usuário e armazenado na variável fat







###############################################################################
print("###############################################################################")


# usando o laço FOR:
# entrada de dados
valor = int(input("informe um valor: ")) # ler o valor e armazenar em uma variável valor
fatorial = 1 # criar uma variável para armazenar o fatorial

# processamento de dados
for i in range(1, valor + 1): # criar um laço para calcular o fatorial do número informado pelo usuário
    fatorial *= i # multiplicar o fatorial pelo número informado pelo usuário

# saida de dados
print(f"O fatorial de {valor} é {fatorial}") # imprimir o fatorial do número informado pelo usuário
print("fim do programa")