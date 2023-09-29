class Conta:
    lista_depositos = []
    lista_saques = []
    def __init__(self, titular_conta, saldo_conta):
        self.titular_conta = titular_conta
        self.saldo_conta = saldo_conta

    def exibir_dados(self):
        print("|---------------------------------------|")
        print("|--Titular: ", self.titular_conta)
        print("|--Saldo: ", self.saldo_conta, "reais.")
        print("|---------------------------------------|")

    def depositar(self):
        depositando = float(input("Quanto você deseja depositar? "))
        self.saldo_conta += depositando
        print("Novo saldo: ", self.saldo_conta, "reais.")
        Conta.lista_depositos.append(depositando)
    def realizar_saque(self):
        saque = float(input("Quanto você deseja sacar? "))
        if saque > self.saldo_conta:
            print("O valor solicitado é maior do que o valor em conta, não é possível sacar!")
            print("Valor disponível em conta: ", self.saldo_conta, "reais.")
        elif saque < self.saldo_conta:
            self.saldo_conta -= saque
            print("Novo saldo: ", self.saldo_conta, "reais.")
            Conta.lista_saques.append(saque)

    def extrato(self):
        print("|---------------------------------------------|")
        print("|----- Saques realizados: ", Conta.lista_saques)
        print("|----- Depósitos realizados: ", Conta.lista_depositos)


conta1 = Conta("Samuel", 100)

opcao = 0
while opcao != 5:
    print("Bem vindo ao sistema bancário!")
    print("1. Consultar Dados / Resumo de Conta.")
    print("2. Realizar Depósito.")
    print("3. Realizar Saque")
    print("4. Extrato de Operações")
    print("5. Sair/Encerrar")
    opcao = int(input("Selecione uma das opções do menu: "))
    if opcao == 1:
        conta1.exibir_dados()
    elif opcao == 2:
        conta1.depositar()
    elif opcao == 3:
        conta1.realizar_saque()
    elif opcao == 4:
        conta1.extrato()
