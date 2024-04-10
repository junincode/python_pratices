n = int(input("Digite o número desejado: "))
c = n
f = n
while c != 1:
    f *= (c-1)
    print("{} X ".format(c), end="")
    c -= 1
print('''1
O fatorial de {} é {}'''.format(n, f))
