n = [0, 1, 1]
def fibonacci():
    while True:
        try:
            c = int(input("Quantos números da sequência deseja ver? "))
        except:
            print("Erro.", end=" ")
        else:
            if c < 0:
                print("Erro. ", end="")
            elif c == 0:
                return[]
            else:
                for i in range(0, c-3):
                    soma = n[-1] + n[-2]
                    n.append(soma)
                break
    return n[0:c]

print(fibonacci())

