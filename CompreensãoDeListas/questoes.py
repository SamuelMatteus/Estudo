#01 - Crie uma lista chamada frutas com 3 elementos do tipo string que representem nomes de frutas.
# Não se esqueça de imprimir a lista.

frutas = ['Banana', 'Maçã', 'Mamão']
print(frutas)

#02 - Crie uma lista chamada numeros com 5 elementos do tipo inteiro.
# Em seguida, imprima apenas o terceiro elemento da lista.

numeros = [1, 2, 3, 4, 5]
print(numeros[2])

#03 - Crie uma lista chamada nomes com 4 nomes de pessoas.
# Em seguida, substitua o segundo nome da lista pelo seu próprio nome.
# Por fim, imprima a lista atualizada.

nomes = ['Pedro', 'Ana', 'João', 'Maria']
nomes.remove('Ana')
nomes.insert(1, 'Samuel')
print(nomes)

#04 - Crie uma lista chamada notas com 5 notas (float) de um aluno.
# Calcule e imprima a média das notas

notas = [5.6, 6.6, 9.2, 8.1, 4.5]
somatorio_notas = sum(notas) / 5
print(somatorio_notas)

#05 - Crie uma lista chamada numeros com os números de 1 a 10.
# Em seguida, imprima apenas os números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[1], numeros[3], numeros[5], numeros[7], numeros[9])


#06 - : Considere a seguinte lista:
# frutas = ['banana', 'maçã', 'uva', 'abacaxi', 'morango'].
# Imprima o primeiro e o último elemento da lista

frutas = ['banana', 'maçã', 'uva', 'abacaxi', 'morango']
print(frutas[0])
print(frutas[4])

#07 - Crie uma lista chamada numeros com os números de 1 a 5.
# Utilize um loop for para imprimir cada número da lista.

numeros_qt07 = [1, 2, 3, 4, 5]
for elemento in numeros_qt07:
    print(elemento)

#08 - Considere a seguinte lista: idades = [18, 25, 32, 47, 53, 60].
# Utilize um loop for para imprimir apenas as idades maiores que 30.

idades = [18, 25, 32, 47, 53, 60]
for maior_que_30 in idades:
    if maior_que_30 > 30:
        print(maior_que_30)

#09 - Considere a seguinte lista: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Utilize o slicing para imprimir os números de 3 a 8.

numeros_qt09 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[2:8])

#10 - Crie uma lista chamada letras com as letras de A a J.
# Utilize o slicing para imprimir as letras de C a G.

letras_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
print(letras_alfabeto[2:7])

#11 - Crie uma lista chamada cores com 5 cores diferentes.
# Utilize o método sort() para ordenar a lista em ordem alfabética.
# Imprima a lista ordenada.

cores = ['Azul', 'Preto', 'Verde', 'Branco', 'Laranja']
cores.sort()
print(cores)

#12 - Crie uma lista chamada numeros com 3 números repetidos.
# Utilize o método count() para contar quantas vezes o número 3 aparece na lista.
# Imprima o resultado.

numeros_qt12 = [4, 4, 4]
resultado = numeros_qt12.count(4)
print(resultado)

#13 - Crie uma lista chamada frutas com 3 elementos.
# Utilize o método append() para adicionar mais uma fruta à lista.
# Imprima a lista atualizada.

frutas_qt13 = ['Maçã', 'Banana', 'Melão']
frutas_qt13.append('Hibisco')
print(frutas_qt13)

#14 - Crie uma lista chamada numeros com os números de 1 a 3.
# Utilize o método reverse() para inverter a ordem dos números na lista.
# Imprima a lista invertida.


numeros_qt14 = [1, 2, 3]
numeros_qt14.reverse()
print(numeros_qt14)

#15 - Crie uma lista chamada animais com 5 elementos.
# Utilize o método pop() para remover o terceiro elemento da lista.
# Imprima a lista após a remoção.

animais = ['Cachorro', 'Gato', 'Pinguim', 'Leão', 'Papagaio']
animais.pop()
print(animais)

