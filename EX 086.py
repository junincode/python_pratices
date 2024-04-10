m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"Digite o valor para a posição[{l}/{c}]: "))
print("-="*20)
for l in range(0, 3):
    print()
    for c in range(0,3):
        print("[ {:^5} ]".format(m[l][c]), end="")
