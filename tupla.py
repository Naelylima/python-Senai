lista = []

# tupla = (1, 2, 3)
# print(tupla)

num = [22, 51, 44, 15]
primeiro = set(num)
seg = {1, 32, 15}

# E; obter todos os numeros sem repetição
print(primeiro | seg)
# O REPITIDO Trazer os numeros que tem nas 2 listas
print(primeiro & seg)
# MENOS O REPITIDO( segundo - primeiro)
print(primeiro - seg)
# TODOS DIFERENTES; trazer elementos diferentes.
print(primeiro^ seg)