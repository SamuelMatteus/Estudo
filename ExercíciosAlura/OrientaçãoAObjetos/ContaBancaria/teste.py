def criar_conta(numero_conta,titular,saldo_conta, limite):
    conta = {"Número": numero_conta, "Titular Conta": titular, "Saldo": saldo_conta, "Limite": limite}
    return conta
def depositar(conta, valor):
    conta["saldo"] += valor

def sacar_valor(conta, valor):
    conta["saldo"] -= valor
def extrato_conta(conta):
    print("Seu saldo é : " + conta["Saldo"])
    