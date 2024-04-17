soma_par = contar_par = 0

for i in range(7):
    numero = int(input(f'digite o {i+1}º número'))

    if numero % 2 == 0:
        soma_par = soma_par + numero
        contar_par += contar_par + 1
print(f'A soma dos {contar_par} é {soma_par}')