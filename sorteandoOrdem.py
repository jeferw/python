import random

pessoas = []
pessoas.append(input('Diga o primeiro nome: '))
pessoas.append(input('Diga o segundo nome: '))
pessoas.append(input('Diga o terceiro nome: '))
pessoas.append(input('Diga o quarto nome: '))

random.shuffle(pessoas)
print('A ordem de apresentação será ')
print(pessoas)
