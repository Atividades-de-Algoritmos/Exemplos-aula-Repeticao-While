#
# Autores:
# Michel Silva
# Carlos Eduardo
# 
# data: 13/07/2022
#
# Material auxiliar (fatorial sem recursão);
# link: https://pt.wikipedia.org/wiki/Fatorial
#
# 4 - Programa que calcule o fatorial de um número.

# [ Usando o laço While ]

# -- Entrada de dados --

numero = int(input('Digite um número inteiro positivo: ')) # Solicitando um valor inteiro do usuário
fatorial = 1 # Inicializar o fatorial com 1

# -- Processamento de dados --

while numero > 0: # Criando um laço para calcular o fatorial do número informado
  
  fatorial = fatorial * numero # Multiplicando o fatorial pelo número informado
  numero = numero - 1 # Decrementando o número informado pelo usuário

# -- Saída de dados --

print('\nO fatorial desse número:', fatorial) # Imprimindo o fatorial
print('\nfim do programa') # Informando ao usuário que o programa terminou


# Versão 2.0 do código

# ------------------------------------------------------------ #

# [ Usando o laço FOR ]

"""# -- Entrada de dados --

valor = int(input("informe um valor: ")) # Solicitando um valor inteiro
fatorial = 1 # Criando uma variável para armazenar o fatorial

# -- Processamento de dados --

for i in range(1, valor + 1): # Criando um laço para calcular o fatorial do número informado pelo usuário
    fatorial *= i # Multiplicando o fatorial pelo número do ciclo atual

# -- Saída de dados --

print(f"\nO fatorial de {valor}!: {fatorial}") # Imprimindo o fatorial do número informado pelo usuário
print("\nfim do programa") # Informando ao usuário que o programa terminou"""

# ------------------------------------------------------------ #
