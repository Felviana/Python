import random

def jogar_jokenpo():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
    while True:
        jogador = input("Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar o jogo): ").capitalize()
        if jogador == "Sair":
            print("Obrigado por jogar!")
            break
        
        if jogador not in ["Pedra", "Papel", "Tesoura"]:
            print("Escolha inválida. Tente novamente.")
            continue
        
        computador = random.choice(["Pedra", "Papel", "Tesoura"])
        print("O computador escolheu:", computador)
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == "Pedra" and computador == "Tesoura") or (jogador == "Papel" and computador == "Pedra") or (jogador == "Tesoura" and computador == "Papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")

if __name__ == "__main__":
    jogar_jokenpo()