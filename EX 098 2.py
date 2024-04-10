def Contador(i, f, p):
    print(f"INICIANDO A CONTAGEM DE {i} ATÉ {f} COM PASSO {p}")
    if p == 0:
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(c, end=" ")
            c += p
    else:
        c = i
        while c >= f:
            print(c, end=" ")
            c -= p
    print()
print("=-"*20)

Contador(1, 10, 1)
Contador(10, 1, 1)
print("=-"*20)
print(f"{"CONTAGEM PERSONALIZADA":^20}")
Contador(int(input("INÍCIO: ")), int(input("FIM: ")), int(input("PASSO: ")))


