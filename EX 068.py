v = 0
from time import sleep
from random import randint
a = " "
while True:
    c = randint(1,10)
    e = input("Quer PAR [P] OU ÍMPAR [I]? ")
    while e not in "IiPp":
        e = input("Error. Quer PAR [P] OU ÍMPAR [I]?")
    n = int(input("Digite um número de 0 a 10: "))
    if e in "Ii":
        a = "ÍMPAR"
    elif e in "Pp":
        a = "PAR"
    print("E...")
    sleep(1)
    print("Você escolheu {}.".format(a.upper()))
    print("A soma entre JOGADOR[{}] e COMPUTADOR[{}] foi {}".format(n, c, c + n))
    if (c + n)%2 == 1:
        if e in "Pp":
            break
        elif e in "Ii":
            print("JOGADOR VENCE.")
            v += 1
    if (c+n)%2 == 0:
        if e in "Pp":
            print("JOGADOR VENCE.")
            v += 1
        elif e in "Ii":
            break
print("=="*20)
print('''O computador venceu.
jogador: [{}]
computador: [{}]
vitórias: {} '''. format(n, c, v))





