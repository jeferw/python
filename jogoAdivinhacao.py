import random
from time import sleep
vlr = random.randint(0, 5)
n = int(input('Adivinhe um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if n == vlr:
    print('Parabéns, vc acertou o número!')
else:
    print('Vc não acertou no número! O correto seria: {}'.format(vlr))
