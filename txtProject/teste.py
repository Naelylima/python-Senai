import bcrypt
class Teste():
    def __init__(self):
        self.aux_nome = []
        self.aux_cpf = []
        self.aux_nascimento = []
        self.lista_cpf = []
        self.user = ''
        self.auxHash = []
        self.senha_digitada = ''
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
            print('----- Cadastro realizado com sucesso -------')

    def ler(self):
        with open('pessoas.txt') as csvfile:
            reader = csvfile.readlines()
            if len(reader) > 0:
                for i in reader:
                    self.lista_cpf = eval(i)
                self.verificar()
            else:
                self.criar_usuario()

    def verificar(self):
        if self.lista_cpf['cpf'] == (self.cpf):
            print('------ Você ja possui cadastro --------')
            self.menu()
        else:
            self.criar_usuario()
            self.menu()



    def gerar_senha(self):
        hashed = bcrypt.hashpw(self.senha.encode('utf8'), bcrypt.gensalt())
        self.senha = hashed

    def ler_usuarios(self):
        with open('pessoas.txt') as csvfile:
            reader = csvfile.readlines()
            if len(reader) > 0:
                for i in reader:
                    # eval converte a string do txt para um dicionario
                    self.lista_cpf = eval(i)
                    self.aux_nome.append(self.lista_cpf['nome'])
                    self.aux_cpf.append(self.lista_cpf['cpf'])
                    self.aux_nascimento.append(self.lista_cpf['nascimento'])
                    self.auxHash.append(self.lista_cpf['senha'])

            aux = 0
            print('--------- Usuários ------')
            for d in range(len(reader)):
                aux += 1
                nomeTESTE = self.aux_nome[d]
                cpfTESTE = self.aux_cpf[d]
                nascimentoTESTE = self.aux_nascimento[d]
                print(f'Usuário {aux}:\nNome: {nomeTESTE}\nCpf: {cpfTESTE},\nNascimento: {nascimentoTESTE}')
                print('-------------------')

            if len(reader) <= 0:
                print('Ainda não existem usuários cadastrados')
                self.inicio()
        self.menu()

    def menu(self):
        print('\n---------- BEM VINDO ----------')
        print('[1] - Mostrar usuarios'
              '\n[2] - Cadastrar usuario')
        escolha = int(input('Digite sua escolha: '))
        if escolha == 2:
            self.inicio()
        elif escolha == 1:
            self.ler_usuarios()
        # elif escolha == 3:
        #     self.entrar()
        else:
            print('---Digite uma opção válida ---')
            self.menu()

    def entrar(self):
        self.user = input('Digite seu usuario: ')
        self.senha_digitada = input('Digite sua senha: ')
        self.valida_senha()

    def valida_senha(self):
        for hash_senha in self.auxHash:
            return bcrypt.hashpw(self.senha_digitada, hash_senha) == hash_senha
        print('foi')

if __name__ == '__main__':
    teste1 = Teste()




