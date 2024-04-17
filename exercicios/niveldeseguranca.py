nome = str(input('Digite seu nome:')).title()
acesso = str(input('Digite seu acesso:')).lower()
if acesso == 'adm' or acesso == "ger" or acesso == "func":
    print(f'Obrigado {nome} você tem acesso ao nosso programa')
      