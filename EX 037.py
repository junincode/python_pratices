n = int(input("Digite um número: "))
print("\033[1;31m[1] BINÁRIO\033[m")
print("\033[1;35m[2] OCTAL\033[m")
print("\033[1;32m[3] HEXADECIMAL\033[m")
r = input("Para qual base você deseja traduzir o número {}?".format(n))
if r == "1":
    print("O número {} em BINÁRIO é {}".format(n, (bin(n)[2:])))
elif r == "2":
        print("O número {} em OCTAL é {}".format(n, oct(n)[2:]))
elif r == "3":
    print("O número {} em HEXADECIMAL é {}".format(n, hex(n)[2:]))
else:
    print("Tente novamente.")