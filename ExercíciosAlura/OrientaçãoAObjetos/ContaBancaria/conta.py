
class Conta:
    def __init__(self, numero_conta, titular, saldo_conta, limite):
        self.__numero = numero_conta
        self.__titular_conta = titular
        self.__saldo_conta = saldo_conta
        self.__limite = limite

    def extrato(self):
        print("Seu saldo é de: " + (self.__saldo_conta) + "Titular: " (self.__titular_conta))

    def depositar(self, valor):
        self.__saldo_conta += valor

    def sacar(self, retirada):
        self.__saldo_conta -= retirada

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo_conta

    def get_titular(self):
        return self.__titular_conta

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite





