import random
from bonecos import*

def comeco():
    print("-"*31)
    print("\n\033[36;40mSEJA BEM-VINDO AO JOGO DA FORCA!\033[m\n")
    print("-" * 31)

def jogo_forca():
    erros = []
    chances = 6
    # ABRINDO ARQ TXT NO PYHTON
    arq = open("palavras")
    palavras_lista = arq.readlines()
    # READLINES TRANSFORMAS EM LISTA
    arq2 = open("dicas")
    dicas = arq2.readlines()
    palavra_aleatoria = random.choice(palavras_lista).replace('\n', '')
    palavra_certa = []

    for i in range(len(palavra_aleatoria)):
        palavra_certa.append(('-'))

    bonecos(chances)
    print('\n\033[36mPalavra:\033[m', '-' * len(palavra_aleatoria))


    while True:
        for j in range(len(palavras_lista)):
            if palavra_aleatoria == palavras_lista[j].replace('\n', ''):
                print(f"\nA dica é: {dicas[j]}")
        letra = input("Digite uma letra: ").upper().replace(" ", "")

        while erros.__contains__(letra) or palavra_certa.__contains__(letra):
            letra = input("Você já digitou essa letra, digite outra diferente: ").replace(" ", "").upper()

        if letra.isdigit():
            print("Digite uma letra, não um número.")
            continue

        if len(letra) > 1:
            print("Digite apenas uma letra.")
            continue

        if palavra_aleatoria.__contains__(letra):
            for pos, encima in enumerate(palavra_aleatoria):
                if letra == encima:
                    palavra_certa.pop(pos)
                    palavra_certa.insert(pos, letra)
            bonecos(chances)
            print("\033[36mPalavra:\033[m ", *palavra_certa)


            if "".join(palavra_certa) == palavra_aleatoria:
                print('\n')
                print("\033[31m*" * 31)
                print("        Você ganhou! :)")
                print("*" * 31,'\033[m')
                escolha()
                break
        else:
            chances -= 1
            bonecos(chances)
            if chances < 1:
                print("\033[31m-" * 31)
                print("       Você perdeu :(")
                print("-" * 31,'\033[m')
                print(f'A palavra certa era: {palavra_aleatoria}')
                escolha()
                break
            erros.append(letra)
            print("\n\033[36mPalavra: \033[m", *palavra_certa)
            print(f"Seus erros são: {erros}")
            print(f"Você errou e tem {chances} chances\n")

def escolha():
    while True:
        decisao = input("\nDeseja continuar? Se sim dê enter, caso não digite 'SAIR': \n").upper().replace(" ", "")
        if decisao == "":
            print('-'*30)
            print('          NOVA RODADA')
            print('-' * 30)
            jogo_forca()
        if decisao == "SAIR":
            break
        else:
            continue

if __name__ == '__main__':
    comeco()
    jogo_forca()
