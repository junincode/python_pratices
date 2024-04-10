im, p = list(), list()
l = list()
l.append(im)
l.append(p)
for i in range(1,8):
    n = int(input(F"{i}-DIGITE UM NÚMERO: "))
    if n%2 == 1:
        im.append(n)
    else:
        p.append(n)
im.sort()
p.sort()
print(F"""OS VALORES PARES FORAM: {p}
OS VALORES ÍMPARES FORAM: {im}""")