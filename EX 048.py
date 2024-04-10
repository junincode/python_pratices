n = 0
i = 0
for c in range(1,501):
    if c%3 == 0 and c%2 == 1:
        n += c
        i += 1
        print(c)
print("{} é a soma de todos os {} n°s ímpares, múltiplos de 3 entre 1 e 500.".format(n, i))
