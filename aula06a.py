# Tipos primitivos e saída de dados personalizada

# Convertendo um valor do tipo string para inteiro:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

total = num1 + num2

print('A soma entre', num1, 'e', num2, 'vale', total)

# .format()
print('A soma entre {} e {} vale {}'.format(num1, num2, total))

# Descobrindo o tipo de dado: Função type():

nome = 'José Rennyer'
idade = 24
peso = 95.7
programador = True

print('{} é do tipo {}'.format(nome, type(nome)))
print('{} é do tipo {}'.format(idade, type(idade)))
print('Peso vale {} e seu tipo é {}'.format(peso, type(peso)))
print(type(programador))

# exibindo uma mensagem maior:

nome_msg = input('Informe o seu nome: ')
idade_msg = int(input('Informe a sua idade: '))
peso_msg = float(input('Informe o seu peso: '))
sonho_msg = str(input('Qual é o seu sonho ? '))

print('Olá, meu nome é {}, eu tenho {} anos, peso {}Kg e meu sonho é {}'.format(nome_msg, idade_msg, peso_msg, sonho_msg))


# Podemos saber o que uma string pode representar e ser:

teste_1 = '12345'
teste_2 = 'Para Você'
teste_3 = '  '
teste_4 = ''
teste_5 = 'abc'
teste_6 = 'A59'
teste_7 = 'Meu País Tem Mais De 200 Milhões De Pessoas'

# para saber se a string pode ser número:
print(teste_1.isnumeric())
print(teste_2.isnumeric())

# Para saber se a string é um espaço em branco
print(teste_3.isspace())
print(teste_4.isspace())

# Para saber se uma string é alpha (letra) e se é alpha numérico (letra ou número ou os dois juntos)
print(teste_5.isalpha()) # ele é apenas letra
print(teste_6.isalpha()) # já ele tem letra e número
print(teste_6.isalnum()) # pois ele é alfa numérico

print(teste_7.isascii()) # vai retornar True apenas se todos os caracteres dessa string pertecerem a tabela ascii
# Ele simplesmente não reconhece como ascii por causa do til em 'milhões' e o acento agudo do í

print(teste_7.istitle()) # Vai verificar se todas as letras inicias de novas palavras são maiúsculas
print('2225'.isnumeric())
print('²'.isnumeric())
print('⅕'.isnumeric()) # isnumeric abrange uma quantidade maior de coisas, incluíndo frações, potência e outros, menos quebrados
print('abc'.isdigit()) # digit também abrange alguns tipos de números e outros números menores

# Já o decimal apenas decimais mesmo, inteiros:
print('24'.isdecimal())
print('10'.isdecimal())
print('56'.isdecimal())