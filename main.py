import random
print("Ola mundo")

nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

if nome == 'natalia':
    print("Você é feia")
else:
    print("Você é bonita ")

if idade == 14:
    print("Vocêbé criança")
else:
    print("Tem mais que 14 ja é gente grande")


aleatorio = random.randint(0, 4)
input(f"{nome} faça uma pergunta: ")

if aleatorio == 1:
    print("SIM")
elif aleatorio == 2:
    print("Talvez sim, talvez não")
elif aleatorio == 3:
    print("Para de ser louca!!")
else:
    print("Não")
