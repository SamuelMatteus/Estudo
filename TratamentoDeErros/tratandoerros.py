def divide_dois_numeros(dividendo, divisor):
    return dividendo/divisor


try:
    numero1 = int(input("Primeiro número: "))
    numero2 = int(input("Segundo número: "))

    resultado = divide_dois_numeros(numero1, numero2)

except TypeError:
    print("Tipos não suportado, erro!")

except ZeroDivisionError:
    print("Divisão por zero não suportado!")


except:
    print("Um erro ocorreu.")

else:
    print(resultado)

finally:
    print("Obrigado por utilizar os serviços, programa encerrado.")


