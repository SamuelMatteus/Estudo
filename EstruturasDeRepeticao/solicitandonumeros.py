#O programa deve solicitar número entre 0 e 10, e armazená-los. Caso seja solicitado um número fora do intervalo,
#ele encerra e automaticamente mostra a soma de todos os números salvos.

lista_guarda_numeros = []
inserir_numero = 0

while inserir_numero < 10:
    inserir_numero = float(input('Insira um número: '))
    lista_guarda_numeros.append(inserir_numero)
    if inserir_numero > 10:
        print("Programa encerrado!")
        break
    total_lista = sum(lista_guarda_numeros)
print("O total dos valores é de: ", total_lista)

