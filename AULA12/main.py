from classes import Veiculo, Carro, Status

marca, modelo, placa, consumo, nivel_combustivel, categoria, airbags, litros_por_mala, conversivel = input('Digite a marca do veículo: '), input('Digite o modelo: '), input("Digite a placa: "), \
                                                   input("Digite o consumo: "), input("Digite o nível de consumo de combustível do carro: "), \
                                                    input("Digite a categoria: "), input("Digite 'sim' se o carro contém airbags e 'não' caso não possua: "), input("Digite quantos litros seu porta-mala contém: "), \
                                                    input("Digite 'sim' caso o seu carro for conversível e 'não' caso não seja: ")


meu_carro = Carro(marca=marca, modelo=modelo, placa=placa, consumo=consumo, nivel_combustivel=nivel_combustivel, categoria=categoria, airbgs=airbags, litros_por_mala=litros_por_mala, conversivel=conversivel)

def cidades_atuais():
    lista_distancias = [230, 199, 220]
    lista_cidades = ["Sumaré", "Campinas", "Hortolândia"]

    print('\n'+'-' * 40)
    cidade_atual = int(input("[1] - "+ lista_cidades[0] +
                         "\n[2] - "+ lista_cidades[1]+
                         "\n[3] - "+ lista_cidades[2]+
                         "\nDigite o número da sua cidade atual: "))
    print('-' * 40)
    destino = int(input("\n[1] - " + lista_cidades[0] +
                             "\n[2] - " + lista_cidades[1] +
                             "\n[3] - " + lista_cidades[2] +
                             "\nDigite o número do seu destino: "))

    if cidade_atual == 1 and destino == 2 or cidade_atual == 2 and destino == 1:
        Status.distancia = lista_distancias[0] - lista_distancias[1]
        print('\n' + '-' * 40)
        print("Sua viagem vai durar em média 30 minutos")
    elif cidade_atual == 2 and destino == 3 or cidade_atual == 3 and destino == 2:
        Status.distancia = lista_distancias[2] - lista_distancias[1]
        print('\n' + '-' * 40)
        print("Sua viagem vai durar em média 20 minutos")
    elif cidade_atual == 3 and destino == 1 or cidade_atual == 1 and destino == 3:
        Status.distancia = lista_distancias[0] - lista_distancias[2]
        print('\n' + '-' * 40)
        print("Sua viagem vai durar média 30 minutos")


def menu():
    while True:
        opcao = int(input("----------------- MENU -----------------\n"
                          "[1] - Acelerar\n"
                          "[2] - Desacelerar\n"
                          "[3] - Manutenção\n"
                          "[4] - Abastecer\n"
                          "[5] - Finanças\n"
                          "Digite o número das opções acima desejada: "))
        if opcao == 1:
            meu_carro.acelerar()
        elif opcao == 2:
            meu_carro.desacelerar()

if __name__ == '__main__':
    cidades_atuais()