def Factorial(n, show=False):
    """
    CALCULA O FATORIAL DO NÚMERO PROPOSTO, MOSTRANDO OU NÃO O CÁLCULO
    :param n: O NÚMERO A SER CALCULADO O FATORIAL
    :param show: VARIÁVEL QUE DECIDE SE O CÁLCULO É MOSTRADO OU NÃO
    :return: SEM RETORNO
    """
    f = 1
    if show == True:
        for c in range(n, 0, -1):
            print(f"{c} X " if c != 1 else f"{c} = ", end="")
            f *= c
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f)


x = int(input("Deseja ver fatorial de qual número? "))
while True:
    v = int(input("Deseja ver o cálculo? [1 = SIM / 0 = NÃO]"))
    if v == 1:
        mostrar = True
        break
    elif v == 0:
        mostrar = False
        break
    else:
        print("ERROR", end=" ")
Factorial(x, mostrar)
