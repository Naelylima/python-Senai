frutas = {'abacaxi': 'abacaxi é uma fruta acida',
          'abacate': 'tem uma barriguinha',
          'limao': 'faça uma limonada'
}

while True:
    usuario = input(f'DIGITE UMA FRUTA: ').lower().strip()
    if usuario not in frutas:
        print('Fruta não cadastrada: ')
        resposta = input('Deseja cadrastra está fruta? sim ou não? ').lower().strip()

        if resposta == 'sim':
            fruta_nova =usuario
            definicao = input('Digite uma definição: ')
            frutas[fruta_nova]= definicao
            print(frutas)
        elif resposta!= 'sim' or resposta != 'não':
            print("Digite SIM ou NÃO\n")
        else:
            break
    else:
        print({frutas[usuario]})
