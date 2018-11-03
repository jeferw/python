def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


num1 = num(input('Informe o primeiro número: '))
num2 = num(input('Informe o segundo número: '))


print('A soma entre {} e {} é: {}'.format(num1, num2, num1 + num2))

