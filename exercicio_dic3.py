#TODO
# Crie duas listas, com 5 valores cada uma.
# Verifique se existe algum número que esteja
# presente nas duas listas e exiba a informação pro
# usuário


set1 = {8, 3, 6, 9, 10}
set2 = {8, 5, 69, 47, 33}
var_aux = set1 & set2

if set1 & set2 :
    print(f"Tem valores iguais, eles são: {var_aux}")
else:
    print('Não existe valores iguias na lista')