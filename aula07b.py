
print('{:-^30}'.format('Operações aritméticas'))
print(2 + 2)
print(10 - 4)
print(6 * 4)
print(7 / 3)
print(5 // 2)
print(16 % 3)
print(4 ** 3)

print('{:-^30}'.format('Ordem de precedência'))

# Ordem de precedência:
print(4 + 2 * 5)
print((4 + 2) * 5)
print(5 - 4 / 2)
print((5 - 4) / 2)
print((10 + 5) * 5 ** 2)

print('{:-^30}'.format('Operador de igualdade'))

# Operador de igualdade:
print(5 == 5)
print(3 == 9)
print(5 + 5 == 10)
n1 = 4
print(n1 * 3 == 15 - 3)
print(n1 + 5 == 10)


print('{:-^30}'.format('Raiz de números'))

# Como saber a raiz de um número: quadrada, cúbida e quarta
print(100 ** (1/2))
print(16 ** (1/2))
print(49 ** (1/2))
print(36 ** (1/2))

print(125 ** (1/3)) # quando se é com um número ímpar como 3, ele meio que quebra
print(64 ** (1/3)) # e por conta disso não dá um valor tão exato
print(12 ** (1/3))

print(256 ** (1/4))
print(120 ** (1/4))


print('{:-^30}'.format('Formatações'))

# Formatações com format
msg = 'algo'

print('{:10}!'.format(msg))
print('{:<10}!'.format(msg))
print('{:^10}!'.format(msg))
print('{:>10}!'.format(msg))

print('{:@<10}!'.format(msg))
print('{:#^10}!'.format(msg))
print('{:=>10}!'.format(msg))

print('{:-^30}'.format('Casas decimais'))

# quantas casas decimais mostrar:
num = 14.567149

print('{:.2f}'.format(num))
print('{:.3f}'.format(num))
print('{:.5f}'.format(num))

print('{:-^30}'.format(' end="" '))

# end=''

print('1 2 3 4 5', end=' >>> ')
print('2 3 4 5 6')

print('José', end=' | ')
print('Rennyer')