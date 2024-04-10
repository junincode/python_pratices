r = " "
mai, men = 0 ,0
c, s = 0, 0
while r not in "Nn":
    c += 1
    n = int(input("Digite o {}° número:".format(c)))
    if c == 1:
        mai = n
        men = n
    s += n
    if n < men:
        men = n
    elif n > mai:
        mai = n
    r = input("DESEJA CONTINUAR? [S/N] ")
    while r not in "SsNn":
        r = input("Error. DESEJA CONTINUAR? [S/N] ")
print('''===============================================
A soma entre todos os {} número(s) digitado(s) é {}
O maior valor digitado é {}
O menor valor digitado é {}'''.format(c, s, mai, men))
