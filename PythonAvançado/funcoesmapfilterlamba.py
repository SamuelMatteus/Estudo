
def tratamento_de_texto(texto):
    return texto.replace('"', '').strip()

lista_exemplo = ['João da Silva, joao"@gmail.com',
                 'Maria da Silva, ma"ria123@email.com',
                 'José de Pau"la,josepaula@email.com']

resultado = list(map(lambda texto: texto.replace('"', '').strip(), lista_exemplo))


print(resultado)

resultado_com_filter = list(filter(lambda lista_exemplo: '@gmail' in lista_exemplo, resultado))
print(resultado_com_filter)