import math

cateto1 = float(input("Insira o valor do primeiro cateto: "))
cateto2 = float(input("Insira o valor do segundo cateto: "))

hipotenusa = math.hypot(cateto1, cateto2)

print(f"O valor da hipotenusa é de: {hipotenusa}")
