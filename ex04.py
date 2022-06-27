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

fat = 1
while numero > 0:
  fat = fat * numero
  numero = numero - 1
print('O fatorial desse número é ', fat)

################   2   ###########################
# se a entrada for ZERO
#entrada
num1 = int(input("informe um número :"))
temp= num1
fat = 1
#processamento
if num1 == 0 :
  pass
else:
  while (num1 > 0):
    fat = fat * num1 # 5*4*3*2*1
    num1 = num1 - 1

#saida
print(f"o fatorial de {temp} é {fat}")





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