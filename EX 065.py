r = " "
m, nc, c, s, st = 1, 0, 1, 0, 0
mai, men, mait, ment = 0, 0, 0, 0
while r not in "Nn":
    c = 1
    while c != 5:
        n = int(input("Digite o {}° valor: ".format(c)))
        s += n
        if c == 1:
            mai = n
            men = n
            if r == " ":
                mait = n
                ment = n
        c += 1
        if n > mai:
            mai = n
        if n < men:
            men = n
    if men < ment:
        ment = men
    if mai > mait:
        mait = mai
    print("="*20)
    print("Dos números digitados: ")
    print("A média entre eles vale {:.2f}".format(s/c))
    print("O maior valor digitado foi {} e o menor foi {}".format(mai, men))
    st += s
    nc += c
    print("="*20)
    r = input("Deseja continuar? [S/N] ")
    while r not in "SsNn":
        r = input("ERROR. Deseja continuar? [S/N] ")
    print("="*20)
print('''AO TOTAL FORAM DIGITADOS {} NÚMEROS
A SOMA TOTAL DE TODOS É {} 
A MÉDIA ENTRE TODOS É {:.2f} 
O MAIOR DE TODOS É {}
O MENOR DE TODOS É {}'''.format(nc, st, st/c, mait, ment))


