# Importando módulos de terceiros e outras práticas minhas mesmo
from math import sqrt, floor
import math

import random

import emoji
import playsound3

# Importando bibliotecas de terceiros: emoji, 

print(sqrt(16))
print(floor(3.57))

print(sqrt(64))
print(math.ceil(3.14))

print(floor(5.95))

print(math.trunc(7.95273))

print(math.pow(4, 3))

print(math.factorial(5))
print(math.factorial(6))

graus = 90
radiano = math.radians(graus)

print(radiano) # serve para converter um ângulo em graus para radianos
# que é basicamente o que as funções de seno, cosseno e tangente precisam:

print('O seno de {}° é: {}'.format(graus, math.sin(radiano)))
print('O cosseno de {}° é: {}'.format(graus, math.cos(radiano)))
print('A tangente de {}° é {}'.format(graus, math.tan(radiano)))



print('==' * 20)
print('Um número aleatório entre 1 e 20: {}'.format(random.randint(1, 20)))
print('Um número aleatório entre 1 e 200: {}'.format(random.randint(1, 200)))
print('Um número aleatorio entre 1 e 2000: {}'.format(random.randint(1, 2000)))
print('Um número bem aleatório: {}'.format(random.random()))

# round() serve para arredondar um número quebrado

num = 5.141598
print(round(num))
print(round(num, 2))
print(round(num, 3))
print(round(num, 4))

print(round(2.5))
print(round(3.5))
print(round(255.5))
print(round(172.5))

# Utilizando uma biblioteca de terceiros: (emoji)

print(emoji.emojize(':melting_face: :sunglasses:'))
print(emoji.emojize("I'm very happy :star_struck: :star_struck:", language='alias'))

# Utilizando a biblioteca para tocar sons (playsound3):

caminho = './16-bits.mp3'
playsound3.playsound(caminho)