import csv
class Teste():
    def __init__(self):
        while True:
            self.nome = input('Digite seu nome: ')
            self.cpf = input('Digite seu CPF: ')
            self.nascimento = input('Digite sua data de nascimento: ')
            if self.nome != '' and self.cpf != '' and self.nascimento != '':
                self.criar_usuario()
                self.ler()
            else:
                pass

    def criar_usuario(self):
        with open('./pessoas.csv', 'a') as csvfile:
            csv.writer(csvfile, delimiter=',').writerow([self.nome, self.cpf, self.nascimento])
    def ler(self):
        with open('./pessoas.csv') as csvfile:
            reader = csv.reader(csvfile)
            for x in reader:
                # if self.cpf.__contains__(x):
                #     print('ja tem')

if __name__ == '__main__':
    teste1 = Teste()
    
#     https://dicasdepython.com.br/como-criar-um-arquivo-csv-no-python/
