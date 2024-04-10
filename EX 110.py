from EX111.UTILIDADE_CEV.MOEDA107 import resumo
r = bool
p = float(input("Digite o preço do produto R$"))
a = int(input("Digite o aumento que deseja simular[0 - 100]%  "))
d = int(input("Digite o desconto que deseja simular[0 - 100]%  "))
while True:
    v = input("Deseja ver o resumo do valor? [1 sim / 0 não] ")
    if v in "10":
        if v == "1":
            r = True
        elif v == "0":
            r = False
        break
    else:
        print("ERROR.", end=" ")
resumo(p, a, d, r)