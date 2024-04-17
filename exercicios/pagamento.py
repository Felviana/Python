preco = float(input('Digite o valor de suas compras R$:'))
print('''Formas de pagamento
      [1] Avista Dinheiro
      [2] Avista Cartão)
      [3] Avista Pix
      [4] 2x no cartão
      [5] 3x ou mais cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total =  (preco * 0.90) 
elif opcao == 2:
    total = (preco * 0.98)   
elif opcao == 3:
    total = (preco * 0.75)   
elif opcao == 4:
    pass
elif opcao == 5:
    total = (preco * 1.20)


print(f'Seu produto de  R$ {preco} com a {opcao} vai custar no final R${total} ') 
