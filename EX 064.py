n, s = 0, 0
c = 1
print("DIGITE 999 quando quiser parar!")
while n != 999:
    n = int(input("Digite o {}° número: ".format(c)))
    if n != 999:
        s += n
        c += 1
print("A SOMA DE TODOS OS {} NÚMEROS DIGITADOS É {}".format(c-1, s))