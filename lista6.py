#TODO Desafio 6
# Faça um programa que ajude o jogador da  Mega Sena a criar palpites. O programa vai  perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo  cadastrando tudo em uma lista composta

import random

# n= 0
#
# print("-"*30)
# print("          MEGA SENA         ")
# print("-"*30)
# jogo = int(input("Quantos jogos você deseja: "))
# print("-"*15, "sorteando",jogo,"jogos")
#
# while jogo != 0:
#     x = random.sample(range(60),6)
#     jogo -= 1
#     n +=1
#     print("jogo", n,":", x)

qtd = int(input("Digite quantos jogos você deseja: "))
lista = []
contador = 1

while True:
    while len(lista) != 6:
        auxiliar = random.randint(1, 60)
        if auxiliar not in lista:
            lista.append(auxiliar)
    print(f'O jogo {contador} é: {lista}')
    contador+=1
    if contador > qtd:
        break



