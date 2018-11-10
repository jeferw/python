a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))

# cada segmento deve ser menor que a soma dos outros dois

if a < (b + c) and b < (c + a) and c < (b + a):
    print('Pode formar um triângulo!')
else:
    print('Não formar um triângulo!')
