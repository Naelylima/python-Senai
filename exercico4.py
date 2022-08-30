#TODO Desafio 4
# Crie um programa que irá ler vários valores numéricos
# colocar em uma, depois disso mostre:
# Quantos números foram digitados
# A lista de valores ordenados de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

lista = []

for f in range(0,5):
    valor = int(input("Digite um valor numerico: "))
    lista.append(valor)
    f+=1
if 5 not in lista:
     print("O 5 não esta na lista")
else:
    print("O 5 está na lista: ")

lista.sort(reverse=True)
print(f'lista contém {f} numeros')
print(f'O reverse da lista é: {lista}')