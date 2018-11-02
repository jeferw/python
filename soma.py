def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


num1 = num(input('Informe o primeiro número: '))
num2 = num(input('Informe o segundo número: '))
soma = num1 + num2
print('A soma é:', soma)
