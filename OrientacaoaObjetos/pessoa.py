#Exercício: Criar uma classe chamada Pessoa com os seguintes atributos: Nome, sobrenome e idade.

class Pessoa:
    def __init__(self, nome, telefone, idade):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade

    def exibir_dados(self):
        print(f'Nome: ', self.nome)
        print(f'Telefone: ', self.telefone)
        print(f'Idade: ', self.idade, 'anos.')







