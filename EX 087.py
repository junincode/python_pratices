s, s3, mai2 = 0, 0, 0
m = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"Digite o valor para a posição[{l}/{c}]: "))
        if m[l][c]%2 == 0:
            s += m[l][c]
        if c == 2:
            s3 += m[l][c]
        if l == 1:
            if c == 0:
                mai2 = m[l][c]
            elif m[l][c] > mai2:
                    mai2 = m[l][c]
print("-="*20)
for l in range(0, 3):
    print()
    for c in range(0,3):
        print("[ {:^5} ]".format(m[l][c]), end="")
print(f"""\nANÁLISE: 
A SOMA DOS VALORES PARES DA MATRIZ É : {s}
A SOMA DOS VALORES DA 3° COLUNA É {s3}
O MAIOR VALOR DA 2° LINHA É {mai2}""")
