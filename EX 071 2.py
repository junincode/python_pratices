v = float(input("Qual valor você deseja sacar? R$"))
c, qc = 100, 0
tot = v
while True:
    if tot >= c:
        tot -= c
        qc += 1
    else:
        if qc > 0:
            if c > 1:
                print(f"{qc} CÉDULA(S) DE R${c}")
            elif c == 1:
                print(f"{qc} MOEDA(S) DE R$1")
            else:
                print(f"{qc} MOEDA(S) DE {c*100:.0f} CENTAVOS")
        if c == 100:
            c = 50
        elif c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        elif c == 1:
            c = 0.50
        elif c == 0.50:
            c = 0.25
        qc = 0
        if tot == 0:
            break