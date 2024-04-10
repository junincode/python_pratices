from random import randint
from time import sleep
tj, j = list(), list()
i = int(input("Quantos jogos deseja sortear? "))
print(F"SORTEANDO {i} JOGOS...")
sleep(1)
for c in range(1, i+1):
    for cont in range(1, 7):
        j.append(randint(1,60))
        while j.count(j[-1]) > 1:
            j.pop()
            j.append(randint(1, 60))
    tj.append(j[:])
    j.clear()
for i, c in enumerate(tj):
    print(f"{i+1}° JOGO... {tj[i]}")
    sleep(0.5)
