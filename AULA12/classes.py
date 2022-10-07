class Veiculo:
    def __init__(self, marca, modelo, placa, consumo, nivel_combustivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.nivel_combustvel = nivel_combustivel

class Carro(Veiculo) :
    def __init__(self, marca, modelo, placa, consumo, nivel_combustivel, categoria, airbgs, litros_por_mala, conversivel):
        super().__init__(marca, modelo, placa, consumo, nivel_combustivel)
        self.categoria = categoria
        self.airbgs = airbgs
        self.litros_por_mala= litros_por_mala
        self.conversivel = conversivel

    def acelerar(self):
        Status.velocidade += 10
        print('-'* 40)
        print("Você está acelerando 10Km/h.")
        print(f"Sua velocidade está em: {Status.velocidade}Km/h.")

    def desacelerar(self):
        Status.velocidade -= 10
        if Status.velocidade <= 0:
            print('-' * 40)
            print('            Você está parado')
        else:
            print('-'* 40)
            print("Você está desacelerando 10Km/h.")
            print(f"Sua velocidade está em: {Status.velocidade}Km/h.")


class Status:
    movimento = False
    distancia = 0
    velocidade = 0
    def __init__(self):
        pass
    def rodou(self, velocidade, distancia):
        rodou = velocidade * 0.1
        distancia -= rodou