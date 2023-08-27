import menuforca
from ExercíciosAlura.JogoDaForca import adivinhando


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        menuforca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhando.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
