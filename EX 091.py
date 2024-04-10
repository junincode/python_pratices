from random import randint
from time import sleep
from operator import itemgetter
jogos = {"jogador1" : randint(1, 6),
         "jogador2" : randint(1, 6),
         "jogador3" : randint(1, 6),
         "jogador4" : randint(1, 6)}
for k, v in jogos.items():
    print(f"{k} tirou {v}")
    sleep(0.75)
rank = sorted(jogos.items(), key = itemgetter(1), reverse=True)
print("=-"*20)
for i, c in enumerate(rank):
    print(f"{i+1}° {c[0]} com {c[1]}")
    sleep(0.75)

