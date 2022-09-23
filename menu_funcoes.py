def menu():
    print("[1]-Listar usuarios"
          "\n[2]-Pesquisar usuario"
          "\n[3]-Adicionar usuario"
          "\n[4]-Atualizar usuario"
          "\n[5]-Sair\n")

def listar_usuarios(n):
    if n == 1:
        print("Você escolheu listar usuarios")
        print(lista)

def pesquisar_usuario(n):
    if n == 2:
        print("Você escolheu pesquisar usuario\n")
        usuario = input("Digite o usuario que deseja pesquisar: ").lower()
        encontrou = False
        for indice_lista, dicionarios in enumerate(lista):
            for index, chave in enumerate(dicionarios):
                if usuario == dicionarios[chave]:
                    encontrou = True
                    print(f'{dicionarios[chave]} está cadastrada\n')

        if encontrou == False:
            print("Esse usuario não existe\n")


def adicionar_usuario(n):
    if n == 3:
        print("Você escolheu adiconar usuario.\n")
        for pos, valor1 in enumerate(dicionario):
            valor = input(f'Por favor digite o {valor1}: ').lower()
            dicionario[valor1] = valor
        lista.append(dicionario.copy())
        print(f'{lista}\n')

def atualizar_usuario(n):
    if n == 4:
        print("Você escolheu atualizar usuario.")
        print(f'{lista}\n')
        usuario = input("Digite o usuario que deseja atualizar: ").lower()
        encontrou = False
        for indice_lista, dicionarios in enumerate(lista):
            for index, chave in enumerate(dicionarios):
                if usuario == dicionarios[chave]:
                    encontrou = True
                    atualizar_salvando(dicionarios, index)

        if encontrou == False:
            print("Esse usuario não existe\n")

def atualizar_salvando(registro, indexLista):
    print(registro)
    campo_atualizar = input("Escreva o que você quer atualizar: ")
    for i, chave in enumerate(registro):
        if  campo_atualizar==chave:
            campo_atualizado =input(f'Escreva o seu {chave}: ')
            registro[chave] = campo_atualizado
            print(registro)
            lista.pop(indexLista)
            lista.append(registro)



if __name__== "__main__":
    lista = []
    dicionario = {'Nome': '', 'Idade': ''}
    while True:
        menu()
        opcao = int(input("Digite a opção desejada: "))
        listar_usuarios(opcao)
        adicionar_usuario(opcao)
        pesquisar_usuario(opcao)
        atualizar_usuario(opcao)
        if opcao == 5:
            break