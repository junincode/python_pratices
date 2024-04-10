l, z = [], 0
for i in range(0,5):
    n = int(input("Digite um número: "))
    if i == 0 or n >= l[-1]:
        l.append(n)
    else:
        while z != len(l):
            if n <= l[z]:
                l.insert(z, n)
                break
            z += 1
print(l)