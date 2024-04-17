def dois_ou_um():
    print("Bem-vindo ao jogo Dois ou Um!")
    print("Cada jogador mostra um número de dedos: 1 ou 2.")

    while True:
        jogador1 = int(input("Jogador 1, quantos dedos você mostra? (1 ou 2): "))
        jogador2 = int(input("Jogador 2, quantos dedos você mostra? (1 ou 2): "))

        soma = jogador1 + jogador2

        if soma % 2 == 0:
            print("A soma dos dedos é par. Jogador 2 vence!")
        else:
            print("A soma dos dedos é ímpar. Jogador 1 vence!")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").upper()
        if jogar_novamente != "s":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    dois_ou_um()