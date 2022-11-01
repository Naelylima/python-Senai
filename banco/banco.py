class SenaiBank:
    agencia = 0
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.__saldo = 1000

    def mostrar_saldo(self):
        return self.__saldo

    def sacar(self, valor_sacar):
            if valor_sacar > self.__saldo:
                return False
            return True

    def efetivar_saque(self, valor_sacar):
        self.__saldo = self.__saldo - valor_sacar
        return self.__saldo

    def depositar(self, deposito, opcao):
        if opcao == 2:
            self.__saldo = self.__saldo + deposito
            return self.__saldo


    def transferir(self, valor_trasferir, opcao):
        if opcao == 3:
            if valor_trasferir > self.__saldo:
                return False
            return True

    def efetivar_transferencia(self, valor_transferir):
        self.__saldo = self.__saldo - valor_transferir
        return self.__saldo

    def extrato(self, opcao):

        if opcao == 4 :
            print('\n******* Você escolheu EXTRATO **********')
            print(f'\nOlá {self.nome}, você possui R$'
                  f'{self.__saldo} na sua conta')
            # print(f'Depositos = {lista1}')
            # print(f'\nSaques = `{lista2}')
            # print(f'\nTransferencias = `{lista3}')
            print('\n*****************************************')
            return self.__saldo


    def menu(self,):
        print('\n[1]-Sacar'
              '\n[2]-Depositar'
              '\n[3]-Transferir'
              '\n[4]-Extrato')

    def asterisco(self):
        print('\n*****************************************')

    def lista_deposito(self, valor):
        lista = []
        lista.append(valor)

    def lista_sacar(self, valor):
        lista = []
        lista.append(valor)

    def lista_transferir(self, valor):
        lista = []
        lista.append(valor)