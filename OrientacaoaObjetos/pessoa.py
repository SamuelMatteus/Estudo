#Exercício: Criar uma classe chamada Pessoa com os seguintes atributos: Nome, sobrenome e idade.

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def exibir_dados(self):
        print(f'Nome: ', self.nome)
        print(f'Sobrenome: ', self.sobrenome)
        print(f'Idade: ', self.idade)

    



