#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 13/07/2022
#
# 3 - Programa que imprime a soma de todos os
# números pares entre dois números quaisquer,
# incluindo-os.

# [ Usando o laço While ]

# -- Entrada de dados --

num1 = int(input('Entre com o valor inicial: ')) # lendo o valor e armazenando em uma variável num1
num2 = int(input('Entre com o valor final: '))  # lendo o valor e armazenando em uma variável num2
soma = 0 # Criando uma variável para armazenar a soma dos números pares entre os valores informados pelo usuário
valor_inicial = num1 # Criando um cópia de num1 para usar no print, já que irá ser alterado no decorrer do código

# -- Processamento de dados --

print() # Deixando um espaço no terminal, como um enter do teclado

while num1 <= num2: # Criando um laço para somar os números pares entre os valores informados pelo usuário
  
  if num1 % 2 == 0: # Se o resto da divisão do número informado pelo usuário por 2 for igual a 0
    print(f'{num1}', end = ' ')
    soma = soma + num1 # Somando o número informado pelo usuário a variável soma
  
  else: # Caso contrário sabemos que o numéro é ímpar
    pass # Nome 'pass' é bem intuítivo, ele apenas passa um ciclo do código while, é um comando omisso

  num1 = num1 + 1  # Ficar atento a identação do bloco para evitar um loop infinito (não precisa ficar no final do laço)

# -- Saída de dados --

print(f"\n\nA soma dos números pares entre {valor_inicial} e {num2}: {soma}") # Imprimindo a soma dos números pares entre os valores informados pelo usuário
print('\nfim do programa') # Informando ao usuário que o programa terminou


# Versão 2.0 do código

# -------------------------------------------------------- #

"""# By Carlos Eduardo

# [ Usando o laço FOR ]

# -- Entrada de dados --

valor1 = int(input("informe um valor: ")) # lendo o valor e armazenando em uma variável valor1
valor2 = int(input("informe um valor: ")) # lendo o valor e armazenando em uma variável valor2
soma = 0 # Criando uma variável para armazenar a soma dos números pares

# -- Processamento de dados --

print() # Print vazio deixa um espaço em branco no terminal, como um enter do teclado

for i in range(valor1, valor2 + 1): # Criando um laço para calcular a soma dos números pares entre os valores informados pelo usuário
    
    if i % 2 == 0: # Se o resto da divisão do número informado pelo usuário por 2 for igual a 0 sabemos que é par
        
        print(f'{i}', end = ' + ') if i != (valor2) else print(i, end = '')  # Imprimindo o número informado pelo usuário
        soma += i # Incrementando a soma dos números pares informados pelo usuário
    
    else: # Se o resto da divisão do número informado pelo usuário por 2 não for igual a 0 sabemos que é número impar
        continue # Volta pro início do for só que agora em outro ciclo

# -- Saída de dados --

print(f"\n\nA soma dos números pares entre {valor1} e {valor2}: {soma}") # imprimir a soma dos números pares entre os valores informados pelo usuário
print("\nfim do programa")"""

# -------------------------------------------------------- #
