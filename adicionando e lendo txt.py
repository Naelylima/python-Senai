import bcrypt
class Teste():
    def __init__(self):
        self.aux = []
        self.lista_cpf = []
        self.primero = True
        self.menu()

    def inicio(self):
        print('\n-------- Cadastro ------------')

        self.nome = input('Digite seu nome: ')
        self.cpf = input('Digite seu CPF: ')
        self.nascimento = input('Digite sua data de nascimento: ')
        self.senha = input('Digite sua senha: ')
        self.ler()


    def criar_usuario(self):
        with open('pessoas.txt', 'a') as csvfile:
            self.gerar_senha()
            dados = dict(nome=self.nome, cpf=self.cpf, nascimento=self.nascimento, senha=self.senha)
            csvfile.write(str(dados) + '\n')



    def ler(self):
        with open('pessoas.txt') as csvfile:
            reader = csvfile.readlines()
            if len(reader) > 0:
                for i in reader:
                    # eval converte a string do txt para um dicionario
                    self.lista_cpf = eval(i)
                    #o teste['cpf'] acessamos o valor da chave CPF do dicionário
                    # print(self.lista_cpf)
                self.verificar()
            else:
                self.criar_usuario()

    def verificar(self):
        if self.lista_cpf['cpf'] == (self.cpf):
            print('------ Você ja possui cadastro --------')
            self.menu()
        else:
            self.criar_usuario()
            print('----- Cadastro realizado com sucesso -------')
            self.menu()



    def gerar_senha(self):
        hashed = bcrypt.hashpw(self.senha.encode('utf8'), bcrypt.gensalt())
        self.senha = hashed

    def menu(self):
        print('\n---------- BEM VINDO ----------')
        print('[1] - Mostrar usuarios'
              '\n[2] - Cadastrar usuario')
        escolha = int(input('Digite sua escolha: '))
        if escolha == 2:
            self.inicio()
        if escolha == 1:
            self.ler_usuarios()


    def ler_usuarios(self):
        with open('pessoas.txt') as csvfile:
            reader = csvfile.readlines()
            if len(reader) > 0:
                for i in reader:
                    # eval converte a string do txt para um dicionario
                    self.lista_cpf = eval(i)
            aux = 0
            print('--------- Usuários ------')
            for d in self.lista_cpf:
                aux += 1
                nomeTESTE = self.lista_cpf['nome']
                cpfTESTE = self.lista_cpf['cpf']
                nascimentoTESTE = self.lista_cpf['nascimento']
                print(f'Usuário {aux}:\nNome: {nomeTESTE}\nCpf: {cpfTESTE},\nNascimento: {nascimentoTESTE}')
                print('-------------------')
            if len(reader) <= 0:
                print('Ainda não existem usuários cadastrados')

        self.menu()


if __name__ == '__main__':
    teste1 = Teste()





