from banco import SenaiBank

nome = input('Ola, digite seu nome: ')
cpf = input('Digite seu CPF: ')
idade = input('Digite sua idade: ')

conta = SenaiBank(nome=nome,
                  cpf=cpf,
                  idade=idade)

while True:
    conta.menu()
    opcao1 = int(input('\nDigite a opção desejada: '))
    conta.extrato(opcao1)
    if opcao1 == 2:
        deposito = int(input('Digite o valor do desposito: '))
        conta.depositar(deposito=deposito, opcao=opcao1)
        conta.asterisco()
        print('\nDeposito realizado com sucesso!\n'
              f'Saldo atual: {conta.mostrar_saldo()}')
        conta.asterisco()

    if opcao1 == 1:
        valor = int(input('Digite o valor que deseja sacar: '))
        if conta.sacar(valor_sacar=valor,):
            conta.asterisco()
            print(f'\nSaque efetivado, Seu saldo é de {conta.efetivar_saque(valor_sacar=valor)}')
            valor = valor * -1
            conta.asterisco()
        else:
            conta.asterisco()
            print('\nValor além do seu saldo\n'
                  f'Saldo atual: {conta.mostrar_saldo()}')
            conta.asterisco()
    if opcao1 == 3:
        valor = int(input('Digite o valo que desseja transferir: '))
        cpf = int(input('Digite o CPF da pessoa que irá receber: '))
        if conta.transferir(valor_trasferir=valor, opcao= opcao1):
            conta.asterisco()
            print(f'\nTranferencia efetivada para o CPF:{cpf}, Seu saldo é de {conta.efetivar_transferencia(valor_transferir=valor)}')
            valor -= valor

            conta.asterisco()
        else:
            conta.asterisco()
            print('\nValor além do seu saldo\n'
                  f'Saldo atual: {conta.mostrar_saldo()}')
            conta.asterisco()




