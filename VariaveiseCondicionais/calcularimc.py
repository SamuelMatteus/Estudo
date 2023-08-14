nome = input("Insira seu nome: ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))

imc = peso / (altura*altura)
print(f"Olá {nome}, este é o seu resultado: ")

if (imc < 17):
    print(imc, "Seu peso está muito abaixo do ideal.")
elif (imc >= 17 and imc < 18.5):
    print(imc , "Seu peso está abaixo do ideal.")
elif (imc >= 18.5 and imc < 25):
    print(imc , "Peso normal.")
elif (imc >= 25 and imc < 30):
    print(imc , "Acima do peso ideal.")
elif (imc >=30 and imc < 35):
    print(imc , "Obesidade grau I")
elif (imc >=35 and imc < 40):
    print(imc , "Obesidade grau II")
elif (imc > 40):
    print(imc , "Obesidade mórbida. Grau III")

