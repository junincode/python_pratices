r = 0
e, c = 1, 1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("\033[1;31mNÚMEROS ESCOLHIDOS: {} E {}\033[m".format(n1, n2))
while r != 5:
    print("="*20)
    print("{}° ESCOLHA.".format(e))
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR")
    print("="*20)
    r = int(input("FAÇA SUA ESCOLHA:  " if c == 1 else "FAÇA SUA ESCOLHA NOVAMENTE: "))
    if r == 1:
        s = n1 + n2
        print("\033[1;31mA soma entre {} e {} vale {}\033[m".format(n1, n2, s))
    elif r == 2:
        m = n1 * n2
        print("\033[1;31mA multiplicação entre {} e {} vale {}\033[m".format(n1, n2, m))
    elif r == 3:
        mai = n1
        if n2 > mai:
            mai = n2
        print("\033[1;31mO maior número entre {} e {} é {}\033[m".format(n1, n2, mai))
    elif r == 4:
        print("OK. FAÇA SUA ESCOLHA NOVAMENTE!")
        print("="*20)
        e += 1
        n1 = int(input("{})Digite o primeiro número: ".format(e)))
        n2 = int(input("{})Digite o segundo número: ".format(e)))
        print("\033[1;31mNÚMEROS ESCOLHIDOS: {} e {}\033[m".format(n1, n2))
    elif r not in (1,2,3,4,5):
        print("CASO DESEJE SAIR, BASTA PRESSIONAR A TECLA 5 NA PRÓXIMA APARIÇÃO DO MENU.")
    c += 1
print("SESSÃO ENCERRADA.")
