km = float(input('Quantos km vc percorreu? '))
dias = int(input('Quantos dias vc usou o carro? '))
precoDia = dias * 60
precoKm = km * 0.15
print('O aluguel deste carro será {:.2f}'.format(precoDia + precoKm))
