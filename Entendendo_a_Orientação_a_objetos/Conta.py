"""Refatoramento a fazer
* Adicionar uma função de criação de conta
* Adicionar funcionalidade ao metodo transferir
* tratar os erros dos valores recebidos da varieavel (valor)
* Decidir aonde vai armazenar as contas criadas(listas, arquivos ou se possivel em um provavel banco de dados)
"""


from time import sleep

def menu(msg,lista, tam=0):
    tam += len(msg)
    print('*' * tam)
    print(msg)
    print('*' * tam)
    print(f'Saque maximo: {Conta.saque_maximo:.2f}R$')
    print(f'Deposito limite: {Conta.deposito_maximo:.2f}R$')
    for i, c in enumerate(lista):
        print(f'{i+1} - {c}')
    print('*' * tam)


def opcao_menu(msg):
    while True:
        try:
            opcao = int(input(msg))
            if opcao > 5:
                raise(opcao)
        except:
            if opcao >= 5:
                print('Opção indisponivel')
            else:
                print('Apenas numeros sao validos.')
            continue
        else:
            return opcao



class Conta:

    saque_maximo = 2000
    deposito_maximo = 5000

    def __init__(self, numero_conta, titular, saldo, limite):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Retirando extrato da conta, Aguarde um momento...')
        sleep(1)
        print('** Extrato **')
        print(f'Conta: {self.__numero_conta}')
        print(f'Titular: {self.__titular}')
        print(f'Saldo: {self.__saldo:.2f}R$')
        print(f'Limite: {self.__limite:.2f}R$')

    def saca(self, valor):
        if valor <= self.saque_maximo:
            if valor <= self.__saldo:
                self.__saldo -= valor
                sleep(1)
                print('Saque efetuado com sucesso...')
                print('Consulte o extrato para ver o saldo.')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor acima do saque permitido')


    def deposita(self, valor):
        if valor <= self.deposito_maximo:
            if valor <= self.__limite:
                self.__saldo += valor
                sleep(1)
                print('Desposito efetuado com sucesso.')
                print('Consulte o extrato para ver o saldo.')
        else:
            print('Valor excedeu o valor de deposito.')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


conta1 = Conta(123, 'Douglas', 5000, 20000)
conta2 = Conta(456, 'Deise', 2500, 20000)
opc = 0
while opc != 5:
    menu('Banco Central', ['Extrato', 'Deposito', 'Saque', 'Transferir', 'Sair'])
    opc = opcao_menu('Digite sua opção: ')
    if opc == 1:
        conta1.extrato()
    elif opc == 2:
        valor = int(input('Digite o valor que deseja deposita:  R$'))
        conta1.deposita(valor)
    elif opc == 3:
        valor = int(input('Digite o valor que deseja sacar:  R$'))
        conta1.saca(valor)
    elif opc == 4:
        pass
    else:
        print('Saindo...')





