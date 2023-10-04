#01 - Crie uma função chamada saudacao que recebe o nome de uma pessoa como parâmetro e imprime a seguinte mensagem:
# “Olá, [nome]!”
def imprimir_nome():
    nome = str(input('Insira seu nome:'))
    print(f"Olá, {nome}")

#02 - Crie uma função chamada soma que recebe dois números como parâmetros e retorna a soma deles.
def receber_dois_valores():
    primeiro = float(input("Insira o primeiro valor: "))
    segundo = float(input("Insira o segundo valor: "))
    resultado = primeiro + segundo
    print(resultado)

#03 - Crie uma função chamada multiplicacao que recebe dois números como parâmetros
# e retorna o resultado da multiplicação deles.
def multiplicar_dois_valores():
    termo1 = float(input("Insira o primeiro valor: "))
    termo2 = float(input("Insira o segundo valor: "))
    multiplicador = termo1 * termo2
    print("O valor multiplicado é igual a: ", multiplicador)

#04 - Crie uma função chamada media que recebe uma lista de números
# como parâmetro e retorna a média aritmética desses números.
def media_valores():
    lista_valores = [2,3,4,5,6]
    total = sum(lista_valores)
    elementos_lista = len(lista_valores)
    media = total / elementos_lista
    print(media)

#05 - Crie uma função chamada maior que recebe uma lista de números como parâmetro
# e retorna o maior número presente nessa lista.
def maior_valor():
    lista_maior = [1,2,3,4,5,6]
    maior = max(lista_maior)
    print(maior)

#06 - Crie uma função chamada verifica_par que recebe um número como parâmetro
# e retorna True se o número for par e False caso contrário.
def verificar_par():
    numero = int(input("Insira o valor: "))
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("Não é par!")

#07 - Crie uma função chamada conta_vogais que recebe uma string como parâmetro
# e retorna a quantidade de vogais presentes nessa string.
def contar_vogais():
    palavra = str(input("Insira a palavra: "))
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    print(f"Essa palavra tem {contador} vogais.")

#7 - : Crie uma função chamada e_primo que recebe um número como parâmetro e retorna True se o número for primo e False caso contrário.
# Um número primo é aquele que só é divisível por 1 e por ele mesmo (por exemplo, 2, 3, 5, 7, 11…).
# def descobrir_numero_primo():
#     numero = int(input("Insira o número: "))
#         if numero

opcao = 0
while opcao != 16:
    print("-------------------------------")
    print("Menu de opções: ")
    print("1. Imprimir seu nome ")
    print("2. Somar dois valores")
    print("3. Multiplicar dois valores")
    print("4. Calcular média de valores")
    print("5. Descobrir o maior valor de um conjunto")
    print("6. Verificar se o número é ou não par")
    print("7. Contador de vogais por palavra")
    print("-------------------------------")
    opcao = int(input("Bem vindo! Selecione a opção conforme o menu:"))

    if opcao == 1:
        imprimir_nome()
    elif opcao == 2:
        receber_dois_valores()
    elif opcao == 3:
        multiplicar_dois_valores()
    elif opcao == 4:
        media_valores()
    elif opcao == 5:
        maior_valor()
    elif opcao == 6:
        verificar_par()
    elif opcao == 7:
        contar_vogais()
