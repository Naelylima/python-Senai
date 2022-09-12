#TODO
# Determine:
# Os valores “ausentes” na lista 2 em comparação com a lista 1 ok
# Os valores “ausentes” na lista 1 em comparação com a lista 2 ok
# Uma lista composta pelos valores únicos existentes na lista1 e lista2
# Uma nova lista que mostre apenas os valores presentes em ambas as listas


lista1 = {28, 34, 55, 41, 9, 71}
lista2 = {9, 31, 44, 74, 28, 56}


print(f'Os valores “ausentes” na lista 2 em comparação com a lista 1 são: {lista1 - lista2}')
print(f'Os valores “ausentes” na lista 1 em comparação com a lista 2 são: {lista2 - lista1}')
print(f'Os valores únicos existentes na lista1 e lista2 são:  {lista1 ^ lista2}')
print(f"Os valores presentes em ambas as listas são: {lista1 & lista2}")