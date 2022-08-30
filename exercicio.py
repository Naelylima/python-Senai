#TODO Exercicio 01- Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No
# final mostre qual foi o maior e menor valor digitado e suas respectivas posições.

lista = []

for f in range(0, 5):
    valor = int(input("Digite um valor númerico: "))
    lista.append(valor)

lista.sort()
print(lista)
# ////////////////////////////////////////////////////

