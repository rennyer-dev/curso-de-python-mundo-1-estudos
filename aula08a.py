# Utilizando módulos
import math # vai importar toda a biblioteca math
import random # isso importa toda a biblioteca random
from random import randint # importa apenas a função randint da biblioteca random

# Função para descobrir a raiz quadrada de um número:
number = 36
raiz_number = math.sqrt(number)

print('A raiz de {} é {}'.format(number, raiz_number))

# Descobrindo a raiz cúbida de um número e também tratando o problema de arredondamento:
number = 64
raiz_number = number ** (1/3)

print('A raiz cúbica de {} é {}, sem arrumar'.format(number, raiz_number)) # sem o arredondamento
print('A raiz cúbica de {} é {}'.format(number, math.ceil(raiz_number)))
# a função ceil vai arredondar o número para cima sempre, vai sempre priorizar o arredondamento
# para cima.

# a função floor, vai ser o contrário de ceil, pois vai arredondar sempre para baixo:
# imagine que eu quero abaixar o preço do valor total da compra para agradar o meu cliente
# que é fiel e sempre compra aqui, porém nesse momento está com pouco dinheiro ¬.¬
valor_total = 3.25
valor_final = math.floor(valor_total)
print('O total da compra era R${}, mas pode ser por R${}'.format(valor_total, valor_final))

# caso queira fazer um arredondamento mais fiel, caso seja acima de 50 vai para cima caso abaixo
# vai para baixo, utilize o round, que não faz parte do math
print('O valor total da compra é de: R${}'.format(round(valor_total, 1)))


# Pegando um número aleatório e decidindo qual será o número de vezes que uma pessoa deverá
# fazer flexões:
nome = 'José Rennyer'
flexoes = randint(1, 25)

print('{} você fará {} flexões, pode começar!'.format(nome, flexoes))

value = random.random()
print(math.trunc(value * 100)) # Só uma tentativa de criar um randint, mesmo já tendo o randint

# sorteando os 6 número da mega-sena .-.
x, y = 1, 60
n1 = random.randint(x, y)
n2 = random.randint(x, y)
n3 = random.randint(x, y)
n4 = random.randint(x, y)
n5 = random.randint(x, y)
n6 = random.randint(x, y)

print('Os números sorteados foram: {}-{}-{}-{}-{}-{}'.format(n1, n2, n3, n4, n5, n6))