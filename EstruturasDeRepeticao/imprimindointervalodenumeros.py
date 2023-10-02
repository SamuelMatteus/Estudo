lista_numeros_anteriores = []
inserir_numero = int(input("Insira um valor: \n"))
i = 1
for i in range(1, inserir_numero + 1):
    lista_numeros_anteriores.append(i)
    print(i)
print(lista_numeros_anteriores)
mostrar_fatorial = int(input('Deseja ver o valor do número que inseriu em fatorial?\n1.SIM\n2.NÃO\n'))
if mostrar_fatorial == 1:
     resultado = 1
     for numero in reversed(lista_numeros_anteriores):
         resultado *= numero
print(resultado)

