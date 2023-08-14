import random
sorteio = random.randint(1, 100)
print("Bem-vindo! Tente adivinhar o número aleatório entre 1 e 100.")

tentativa = int(input("Qual é o seu palpite? "))

if (tentativa == sorteio):
    print("Parabéns, você acertou!")
else:
    print(f"Errado! O número sorteado era {sorteio}")

