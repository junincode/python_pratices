from time import sleep
def Contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p} >>>>>>>")
    print("    ", end="")
    if p > 0:
        for c in range(i, f+1, p):
            print(c, end=" ")
            sleep(0.25)
    if p < 0:
        for c in range(i, f-1, p):
            print(c, end=" ")
            sleep(0.25)
    print("FIM!")
    print("=-"*20)
Contador(1, 10, 1)
sleep(2)
Contador(10, 0, -2)
sleep(2)
print("\nAgora você escolhe >>>>")
Contador(int(input("INÍCIO:")), int(input("FIM: ")), int(input("PASSO: ")))
sleep(1)
print("\n<<<FIM>>>")


