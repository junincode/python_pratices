import random as r
res = ""
qv = 0
while res.lower() != "n":
    print("""[1] PEDRA
[2] PAPEL
[3] TESOURA""")
    while True:
        ME = int(input("Faça sua escolha: "))
        print("=="*20)
        if ME not in (1, 2, 3):
            print("Error.", end=" ")
        else:
            break

    EC = r.choice(["PEDRA", "PAPEL", "TESOURA"])

    #Casos que o jogador ganha:

    if (ME == 1 and EC == "TESOURA") or (ME == 2 and EC == "PEDRA") or (ME == 3 and EC == "PAPEL"):
        print("O JOGADOR VENCEU!")
        qv +=1
    elif (ME == 1 and EC == "PEDRA") or (ME == 2 and EC == "PAPEL") or (ME == 3 and EC == "TESOURA"):
        print("EMPATE!")
    else:
        print("O COMPUTADOR VENCEU!")
    print("O jogador escolheu", "PEDRA" if ME == 1 else "PAPEL" if ME == 2 else "TESOURA" if ME == 3 else None)
    print(f"O computador escolheu {EC}")
    res = str(input("Deseja continuar [S/N]? "))
print(f"Você venceu {qv} vez(es)")
