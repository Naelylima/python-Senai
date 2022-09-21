def find1():
    lista = []
    palavra_secreta = "pythonetscampinas".lower()
    for pos, letra in enumerate(palavra_secreta):
        if letra == 's':
            lista.append(pos)
    print(f'o "S" está nas posições: {lista}')
    qtd = len(lista)
    print(f'A quantiddae de "S" é: {qtd}')


if __name__ == '__main__':
    find1()
