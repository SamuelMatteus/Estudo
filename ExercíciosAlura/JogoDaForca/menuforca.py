import random
def exibir_menu():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("***  Adivinhe qual é a fruta! ***")
    print("*********************************")
def abrir_arquivo_e_carregar_palavra():
    arquivo = open("ListaDePalavras.txt", "r")
    lista_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()
    elemento = random.randrange(0,len(lista_palavras))
    palavra_secreta = lista_palavras[elemento].upper()
    return palavra_secreta
def inserir_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def jogar():
    exibir_menu()
    palavra_secreta = abrir_arquivo_e_carregar_palavra()
    letras_acertadas = inserir_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            indice = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[indice] = letra
                indice += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Lamento, você perdeu, a palavra correta era {palavra_secreta.lower().capitalize()}")
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
