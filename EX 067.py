c, z = 1, 0
while True:
    z += 1
    n = int(input("{}-De qual n° deseja ver a tabuada? ".format(z)))
    if n < 0:
        break
    for c in range(1,11):
        print(" {} X {} = {} ".format(n, c, n*c))
print("Fim do programa.")

