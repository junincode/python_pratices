from random import randint as r
def sorteia(l):
    sp = 0
    print("Sorteando 5 valores...", end=" ")
    for c in range(0, 5):
        l.append(r(0, 10))
        print(l[c], end=" ")

lista = list()
sorteia(lista)
def SomaPar(l):
    sp = 0
    for c in l:
        if c%2 == 0:
            sp += c
    print(f"\nDentre os valores {l} ==> A soma dos pares resultou em {sp}")

SomaPar(lista)