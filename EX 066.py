s, c = 0, 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    c += 1
    s += n
print("A soma de todos os {} n°s vale {}".format(c, s))
