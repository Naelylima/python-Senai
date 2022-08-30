#TODO EXERCICO 2- Crie um programa que permita ao usuário digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em
# ordem crescente.

lista = []

for f in range(0, 5):
    valor = int(input("Digite um valor númerico: "))
    if valor not in lista:
        lista.append(valor)
lista.sort()
print(lista)