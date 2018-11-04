n = int(input('Informe um número: '))
i = 1
print('=' * 20)
while i <= 10:
    print('{} x {:>2} = {:>3}'.format(n, i, (n * i)))
    i += 1
print('=' * 20)
