def LeiaInt(a):
        while not a.isnumeric():
            print("\033[1;31mERRO. DIGITE UM NÚMERO INTEIRO.\033[m")
            a = (input("Digite um número: "))
        print(f"Você acabou de digitar o número {a}")


n = input("Digite um número: ")
LeiaInt(n)