# Manipulando strings/texto

frase = 'Programação é Legal'

# Fatiamento
print(frase[0])
print(frase[8])

print(frase[0:6]) # O índice final sempre é ignorado, e ele pega o antes dele
print(frase[6:11])
print(frase[:11])
print(frase[14:])

print(frase[0:11:2]) # do 0 ao 11 pulando de 2 em 2 
print(frase[::])
print(frase[::4])
print(frase[:11] + frase[14:])
print(frase[:3] + frase[6:11] + ' ' + frase[14:])
print('{}{}{}{}{}'.format(frase[:3], frase[6:7], frase[2:3], frase[8:11], frase[11:]))

print(frase[::-1]) # Vendo uma string de trás para frente


# Analise de string
print(len(frase))
frase_sem_espacos = ''.join(frase.split()) # Contando apenas os caracteres de uma string
print('"{}" tem {} letras'.format(frase, len(frase_sem_espacos)))
print(frase.count('a'))

print(frase.find('programação'))
print(frase.lower().find('programação'))
print('Programação' in frase) # Verificando se a string 'Programação' está presente em frase
print('legal' in frase) 

# Transformação

print(frase.replace('Legal', 'Magnífica'))
print(frase.replace('é Legal', 'é Muito Legal'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # Transforma apenas a primeira letra da string inteira em maiúscula
# Já o title() capitaliza toda ela de fato, a cada palavra, a primeira letra fica maiúscula
print(frase.title())

frase = '           meu nome é Rennyer      '
print(frase.rstrip())
print(frase.lstrip())
print(frase.strip().upper())

# Dividindo uma string
frase = 'Eu gosto muito de programar em python'
frase_quebrada = frase.split() # Por padrão o argumento é um espaço em branco
print(frase_quebrada)
print(frase.split('o')) # quebrando através da letra 'o'
print(frase.split('a'))


# Juntando uma string que foi transformada em lista de strings
print('_____'.join(frase.split()))
print('='.join(frase.split()))

# String gigante: """"""

frase = '''
    Essa é apenas uma string maior para dizer o quanto
    Está sendo bacana aprender python, e aprender programação
    Do zero com um dos melhores professores de programação
    Do brasil o famoso Gustavo Guanabara, ele é muito legal
    Um grande professor, e está ensinando muito bem essa
    Linguagem incrível e que eu gosto tanto o Python ^^
'''

print(frase)
print(len(frase))
print(frase.split())
print('Essa frase tem {} caracteres!'.format(len(''.join(frase.split()))))
apenas_letras = ''.join(''.join(frase.split()).split(',')).replace('^^', '')
print(apenas_letras)
print(len(apenas_letras))