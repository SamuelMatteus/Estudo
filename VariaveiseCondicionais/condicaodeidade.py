nome = input("Olá, qual é o seu nome? ")
idade = int(input("E qual é a sua idade? "))

if (idade < 18):
    print(f"Lamento {nome}! \nVocê não pode acessar nosso site.")
else:
    print(f"Olá, {nome}! \nSeja bem vindo ao nosso site.")