def teste():
    dicionario = {}
    lista = []

    while True:
        campo = input("Digite o nome do campo desejado: ")
        if campo == "":
           break
        dicionario[campo] = ""
    while True:
        for x, y in enumerate(dicionario):
            valor = input(f'Por favor digite o {y}: ')
            dicionario[y] = valor
        lista.append(dicionario.copy())
        sair = input("Digite enter para continuar e qualquer letra para sair: ")
        if sair != "":
            break
    print(lista)


if __name__ == "__main__":
    teste()