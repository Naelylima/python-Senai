# Desafio 5
#TODO Crie um programa que irá ler vários valores numéricos colocar em uma
# lista, depois disso crie 2 listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# ● Ao final mostre o conteúdo das 3 listas geradas


lista3 = []
lista2 = []
lista = []


for f in range(0, 5):
    num = int(input("Digite um valor: "))
    lista.append(num)

    if num %2 ==0:
        lista2.append(num)
    else:
        lista3.append(num)

print(f'Lista total: {lista}')
print(f'Lista de pares: {lista2}')
print(f'Lista dos impares: {lista3}')
