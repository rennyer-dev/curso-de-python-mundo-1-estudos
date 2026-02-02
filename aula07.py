# Operadores aritméticos
# + -> Soma
# - -> Subtração
# * -> Multiplicação
# / -> Divisão
# // -> Divisão inteira
# % -> módulo
# ** -> Potência

n1 = 5
n2 = 4

print('{} + {} = {}'.format(n1, n2, n1 + n2))
print('{} - {} = {}'.format(n1, n2, n1 - n2))
print('{} * {} = {}'.format(n1, n2, n1 * n2))
print('{} / {} = {}'.format(n1, n2, n1 / n2))
print('{} // {} = {}'.format(n1, n2, n1 // n2))
print('{} ** {} = {}'.format(n1, n2, n1 ** n2))
print('{} % {} = {}'.format(n1, n2, n1 % n2))

# ordem de precedência:
# 1º ()
# 2º **
# 3º * / // %
# 4º + -

print(5 + 2 * 4) # não vai dar 28, mas sim 13, pois a multiplicação vem primeiro que a adição
print((5 + 2) * 4) # Agora sim 28

print(5 * 5 + 4 ** 3) # 1º ** 2º * 3º +     89
print(5 * (5 + 4) ** 3) # 3645 O_o fiz na calculadora...

# python suporta calculos com números gigantes e astronômicos:

print(23 ** 50)

print(3 * 3 / 5 + 4 * 3 ** 2 + 5 / (10 + 5 - 1)) # ?


# temos o operador de igualdade == para checar se um valor é igual ao outro

print(5 + 4 == 6 + 3)
print(8 + 8 == 10 + 6)
print(3 == 2)
print(15 + 1 == 15 + 0)


# Para sabermos a raiz quadrada de um número
# eleve o número a meio (1/2)
# 25, 49, 127, 81, 225, 1000, 

print(25 ** (1/2)) # raiz quadrada de 25
print(49 ** (1/2)) 
print(127 ** (1/2))
print(81 ** (1/2))
print(225 ** (1/2))
print(1000 ** (1/2))

# Imagine que eu quero saber agora a raiz cúbida, ou seja ³

print(125 ** (1/3)) # Nesse caso deu 4.999999 mais por bug da própria linguagem em relação a números
# com pontos flutuantes

# raiz quarta
print(256 ** (1/4))

# Formatando a saída de outras formas:
msg = 'Seja bem vindo'

print('{:=^40}'.format(msg)) # dessa forma o conteúdo vai para o centro, tem o espaço
# de 40 caracteres, e está alinhado ao meio

# como decidir quantas casas decimais serão exibidas:
# vamos calcular o imc:

peso = 95.7
altura = 1.83
imc = peso / (altura ** altura)

print(imc) # sem format
print('{:.2f}'.format(imc)) # mostrando apenas 2 casas decimais


# end= com ele podemos decidir o que vai acontecer ao final da linha
nome = 'José'
sobrenome = 'Rennyer'
print('Meu nome é {}'.format(nome), end=' ')
print(sobrenome)

print('Me chamo {} {}, moro no brasil e gosto bastante de aprender'.format(nome, sobrenome), end=' ')
print('programação, pois me faz pensar melhor, ter uma lógica melhor e construir muitas coisas!')

# Qualquer coisa pode ser referênciada ao final:

n1, n2 = 5, 6
sum = n1 + n2

print('{} & {}'.format(n1, n2), end=' >>> ')
print('{} + {} = {}'.format(n1, n2, sum))