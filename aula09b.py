# Pratica 2

frase = 'Nunca Desista'
print(frase[4])
print(frase[9])
print(frase[-1])

print('=' * 30)
# Com range:
print(frase[2:9])
print(frase[0:5])
print(frase[0:4])
print(frase[6:])
print(frase[7:])
print(frase[:3])
print(frase[:9])
print(frase[0:10])

# Com passos
print(frase[0:10:2])
print(frase[::3])
print(frase[::-1])

print('=' * 30)

palavra = 'Tesoura'
print(len(palavra))

objeto = 'Paralelepipedo'
print(objeto.count('e'))
print(objeto.count('e', 9, 14))

print(objeto.find('pipe'))
print(objeto.find('qua'))

print('Quadrado' in objeto)
print('Parale' in objeto)

# Transformação

palavra = 'Maçã é Bom'
print(palavra.upper())
print(palavra.lower())
print(palavra.capitalize())
print(palavra.title())
print(palavra.replace('Bom', 'Deliciosa'))

palavra = '    Algo    '
print(palavra.strip())
print(palavra.rstrip())
print(palavra.lstrip())

palavra = 'bom e legal'
print(palavra.split())
print(palavra.split('e'))

lista = ['eu', 'gosto', 'de', 'jogar']
print('-'.join(lista))

frase_formatada = '''Eu
Sou
Um
Programador
Bem
Legal'''
print(frase_formatada)