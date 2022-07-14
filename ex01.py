#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 13/07/2022
#
# 1 - Programa que imprime a quantidade de números
# pares de 100 até 200, incluindo-os.

# [Usando o laço While]

# Entrada de dados

num = 100 # Criando uma variável para armazenar o número inicial.
contadorPares = 0 # Criando uma variável para armazenar a quantidade de números pares entre 100 e 200.

# Processamento de dados

while num <= 200: # Criando um laço while, enquanto variavel 'num' for menor igual que 200 o código irá executar
  
  if num % 2 == 0: # Se o número é múltiplo de 2 temos que o número é par
    contadorPares = contadorPares + 1 # Incrementar a quantidade de números pares informados pelo usuário + 1
  
  else: # Caso contrário irá executar o comando pass que somente passa um ciclo do nosso while
    pass

  num = num + 1 # Ficar atento a identação do bloco para evitar um loop infinito

# Saída de dados

print(f'Quantidade de números pares entre 100 e 200: {contadorPares}') # Imprimindo a quantidade de números pares entre 100 e 200 incluindo-os
print("\nfim do programa")


# Versão 2.0 do código

# -------------------------------------------------- #

# [Usando o laço FOR]

"""# Entrada de dados

quantidade = 0 # Criando uma variável para armazenar a quantidade de números pares

# Processamento de dados

for i in range(100, 201): # Criando um laço para calcular a quantidade de números pares de 100 até 200 passando-os como parâmetro pra função range()
    
    if i % 2 == 0: # Se o resto da divisão do número informado pelo usuário por 2 for igual a 0
        print(f'{i}', end = ' ') # Imprimindo o número informado pelo usuário
        quantidade += 1 # Incrementar a quantidade de números pares informados pelo usuário
    
    else: # Caso contrário sabemos que nosso número é impar, então executa a indentação
        continue # Volta pro início do for

# Saída de dados

print(f"\n\nA quantidade de números pares de 100 até 200: {quantidade}")
print("\nfim do programa")
"""
