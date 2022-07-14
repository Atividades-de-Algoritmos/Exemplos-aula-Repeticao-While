#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 13/07/2022
#
# 2 -programa para contar a quantidade de números
# pares entre dois números quaisquer?

# [Usando o laço While]

# -- Entrada de dados --

num1 = int(input('Entre com o valor inicial: ')) # Solicitando o valor e armazenando em uma variável num1
num2 = int(input('Entre com o valor final: ')) # Solicitando o valor e armazenando em uma variável num2
valor_inicial = num1 # Criando um cópia de num1 para usar no print, já que irá ser alterado no decorrer do código

if num2 < num1: # Se o valor de parada informado for menor do que o inicial não temos intervalo, então irá gerar um erro
  print('\nO valor de parada é menor do que o inicial !!!') # Imprimindo o erro no terminal

elif num2 == num1: # Se o valor de para informado for igual ao do inicial também não temos intervalo, então irá gerar outro erro.
  print('\nO valor de parada é igual ao do inicial !!!')

else: # Caso contrário, significa que não temos erro no programa
  pass # O nome é intuítivo, 'pass' só irá passar e executar o código normalmente. 

contadorPares = 0 # Criando uma variável para armazenar a quantidade de números pares entre os valores informados pelo usuário

# -- Processamento de dados --

print() # Deixando uma linha no terminal, como um enter do teclado

while num1 <= num2: # Criando um laço para contar a quantidade de números pares entre os valores informados pelo usuário

  if num1 % 2 == 0: # Sabemos quando é par quando um número é divisível por 2
    print(f'{num1}', end = ' ')
    contadorPares += 1 # Incrementando a quantidade de números pares informados pelo usuário
  
  else: # Caso contrário executa a identação
    pass # o nome 'pass' é bem intuítivo, ele apenas passa um ciclo do código while, é comando omisso
  
  num1 += 1 # Ficar atento a identação do bloco para evitar um loop infinito

# -- Saída de dados --

print(f'\n\nA quantidade de números pares entre {valor_inicial} e {num2}: {contadorPares}') # Imprimindo a quantidade de números pares entre os valores informados pelo usuário
print('\nfim do programa')

# Versão 2.0 do código

# ------------------------------------------------------------------- # 

# [Usando o laço FOR]

"""# -- Entrada de dados --

valor1 = int(input("informe um valor: ")) # lendo o valor e armazenando em uma variável valor1
valor2 = int(input("informe um valor: ")) # lendo o valor e armazenando em uma variável valor2
quantidade = 0 # Criando uma variável acumuladora para armazenar a quantidade de números pares

if valor2 < valor1: # Se o valor de parada informado for menor do que o inicial não temos intervalo, então irá gerar um erro
  print('\nO valor de parada é menor do que o inicial !!!') # Imprimindo o erro no terminal

elif valor2 == valor1: # Se o valor de para informado for igual ao do inicial também não temos intervalo, então irá gerar outro erro.
  print('\nO valor de parada é igual ao do inicial !!!')

else: # Caso contrário, significa que não temos erro no programa
  pass # O nome é intuítivo, 'pass' só irá passar e executar o código normalmente. 

# -- Processamento de dados --

print() # Deixando uma linha, como se fosse um enter do teclado

for i in range(valor1, valor2 + 1): # Criando um laço para calcular a quantidade de números pares entre os valores informados pelo usuário, ou seja, x e y
    
    if i % 2 == 0: # Sabemos que é par quando o número é divisível por 2
        print(f'{i}', end = ' ') # Imprimindo o número informado pelo usuário
        quantidade += 1 # Incrementando a quantidade de números pares informados pelo usuário
    
    else: # Caso contrário sabemos que o numéro é impar
        continue # Volta pro começo do for só que agora em outro ciclo

# -- Saída de dados --

print(f"\n\nA quantidade de números pares entre {valor1} e {valor2}: {quantidade}") # Imprimindo a quantidade de números pares entre os valores informados pelo usuário
print("\nfim do programa")"""

# ------------------------------------------------------------------- #
