from time import sleep
print("Aqui estão todos os pares entre 1 e 50")
n = 0
for c in range(1,51,):
    if c%2 == 0:
        n += 1
        print(c, end= ' ')
        sleep(0.20)
print("Há no total {} n°s pares".format(n))