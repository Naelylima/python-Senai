import math


def potenciacao(numero, numero2):
    resultado = numero ** numero2
    print(f'O resultado é: {resultado}')


def raiz(numero, numero2):
    raiz1 = math.sqrt(numero)
    raiz2 = math.sqrt(numero2)
    print(f'A raiz de {numero} é {raiz1}'
          f' já a raiz de {numero2} é {raiz2}')


def porcentagem(numero, numero2):
    resultado = numero * (numero2 / 100)
    print(f'resultado da porcentagem de {numero} é :'
          f'é {resultado}')


numero = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))

while True:
    opcao = int(input('''Escolha uma opção:             
                           [1]Potência
                           [2]Raiz
                           [3]Porcentagem

     DIGITE UM OPÇÃO:  '''))

    if opcao == 1:
        potenciacao(numero, numero2)
        break
    elif opcao == 2:
        raiz(numero, numero2)
        break
    elif opcao == 3:
        porcentagem(numero, numero2)
        break
    else:
        print("Opção invalida")


