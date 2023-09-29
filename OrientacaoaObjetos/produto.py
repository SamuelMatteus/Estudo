class Produto:
    def __init__(self, nome, estoque, descricao, preco):
        self.nome = nome
        self.estoque = estoque
        self.descricao = descricao
        self.preco = preco

    def mostrar_nome(self):
        print('Preço: ', self.preco)

    def mostrar_estoque(self):
        print('Quantidade em Estoque: ', self.estoque)

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        novo_nome = str(input('Insira o novo nome do produto: '))

    def alterar_estoque(self, novo_estoque):
        self.estoque = novo_estoque

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def alterar_descricao_produto(self, nova_descricao):
        self.descricao = nova_descricao

    def apresentar(self):
        print("Nome: ", self.nome)
        print("Quantidade em estoque: ", self.estoque, "unidades.")
        print("Descrição: ", self.descricao)
        print("Preço: ", self.preco)




produto1 = Produto("Celular Samsung", 12, "Aparelho celular produzido em 2023", 4330.0)
