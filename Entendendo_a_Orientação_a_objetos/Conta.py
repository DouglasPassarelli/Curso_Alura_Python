from time import sleep

class Conta:

    def __init__(self, numero_conta, titular, saldo, limite):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Retirando extrato da conta, Aguarde um momento...')
        sleep(1)
        print('** Extrato **')
        print(f'Conta: {self.numero_conta}')
        print(f'Titular: {self.titular}')
        print(f'Saldo: {self.saldo}')
        print(f'Limite: {self.limite}')



conta1 = Conta(123, 'Douglas', 1000, 2000)
conta1.extrato()
