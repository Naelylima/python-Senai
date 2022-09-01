#TODO Exercico 3 -Crie um programa que permita ao usuário digitar 5 valores numéricos e cadastre-os em
# uma lista já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.

lista = []

for f in range(0, 5):
    valor = int(input("Digite um valor númerico: "))
    if f ==0 or valor> lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos <len(lista):
            if valor<= lista[pos]:
                lista.insert(pos, valor)
                break
            pos+=1

print("-"*30)
print(lista)

