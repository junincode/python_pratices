import time
from random import choice
c = ["PEDRA", "PAPEL", "TESOURA"]
e = choice(c)
print("="*20)
print("{:^30}".format("\033[1;35mJOKENPÔ\033[m"))
print("="*20)
print("[1] PEDRA")
print("[2] PAPEL")
print("[3] TESOURA")
n = int(input(("FAÇA SUA ESCOLHA: ")))
if n == 1:
    n = "PEDRA"
elif n == 2:
    n = "PAPEL"
elif n == 3:
    n = "TESOURA"
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
print("="*20)
print('''COMPUTADOR ESCOLHEU {}
JOGADOR ESCOLHEU {}'''.format(e, n))
print("="*20)
if n == e:
    print("\033[1;34mEMPATE!\033[m")
elif (e == "PAPEL" and n == "PEDRA") or (e == "PEDRA" and n == "TESOURA") or (e == "TESOURA" and n == "PAPEL"):
    print("\033[1;31mEU VENCI!\033[m")
elif not n in ("TESOURA PAPEL PEDRA"):
    print("Opção inválida.")
else:
    print("\033[1;32mVOCÊ VENCEU!\033[m")
