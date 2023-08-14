nome = input("Olá, qual é o seu nome? ")
sobrenome = input("Informe também seu sobrenome: ")
salario_atual = float(input("E qual o seu salário atual? "))

cenario_10 = 0.10
cenario_25 = 0.25
cenario_30 = 0.30
cenario_50 = 0.50

print(f"Olá {nome} {sobrenome}\n"
      f"Seu salário com 10% de aumento fica no valor de: {salario_atual + (salario_atual * cenario_10)}\n"
      f"Seu salário com 25% de aumento fica no valor de: {salario_atual + (salario_atual * cenario_25)}\n"
      f"Seu salário com 30% de aumento fica no valor de: {salario_atual + (salario_atual * cenario_30)}\n"
      f"Seu salário com 50% de aumento fica no valor de: {salario_atual + (salario_atual * cenario_50)}\n")