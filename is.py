var = input('Informe algo: ')

print('O tipo de {0} é {1}!'.format(var, type(var)))
print('{}, é um número? {}!'.format(var, var.isnumeric()))
print('{}, é uma palavra? {}!'.format(var, var.isalpha()))
print('{}, possui somente espaços? {}!'.format(var, var.isspace()))
print('{}, está somente em maisculo? {}!'.format(var, var.isupper()))
print('{}, está somente em minusculo? {}!'.format(var, var.islower()))
print('{}, é letras e números? {}!'.format(var, var.isalpha()))
