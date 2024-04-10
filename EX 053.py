ac = []
f = input("Digite um frase: ")
t = len(f.replace(" ", "")) - 1
for c in range(1, len(f.replace(" ", "")) + 1):
    ac.insert(c-1, f.replace(" ", "")[t])
    t -= 1
p = "".join(ac)
print("\033[1;34m{}\033[m ao contrário é \033[1;33m{}\033[m".format(f.replace(" ", ""), p))
if p == f.replace(" ", ""):
    print("{} é um PALÍNDROMO!".format(f))
else:
    print("Não é um PALÍNDROMO!")
