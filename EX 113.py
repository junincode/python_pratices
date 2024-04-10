n, n2 = 0, 0
def LeiaInt():
    global n
    while True:
        try:
            n = int(input("Digite um número: "))
        except:
            print("\033[1;31mHouve um problema na introdução de dados.\033[m")
        else:
            print(f"Número {n} computado!")
            break
LeiaInt()
print(f"Fora da função, o número {n} foi armazenado.")
def Leiafloat():
    global n2
    while True:
        try:
            n2 = float(input("Digite um número decimal: "))
        except:
            print("\033[1;31mHouve um problema na introdução de dados.\033[m")
        else:
            print(f"Número {n2} computado!")
            break
print("=-"*30)
Leiafloat()
print(f"Fora da função, o número {n2} foi armazenado.")