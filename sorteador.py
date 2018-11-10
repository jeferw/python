import random

pessoas = []
pessoas.append(input('Diga o primeiro nome: '))
pessoas.append(input('Diga o segundo nome: '))
pessoas.append(input('Diga o terceiro nome: '))
pessoas.append(input('Diga o quarto nome: '))

# print('O sorteado foi: {}'.format(pessoas[random.randrange(len(pessoas))]))
print('O sorteado foi: {}'.format(random.choice(pessoas)))
