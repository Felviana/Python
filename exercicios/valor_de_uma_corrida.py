km = float(input('Rodou quantos km rodou:  '))
if km<=150:
    valor = km * 0.50
else:
    valor = 150 * 0,50 + (km - 150) * 0.80
print('O valor total a ser pago é de R$', valor)

