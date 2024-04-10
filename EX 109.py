from EX111.UTILIDADE_CEV.MOEDA107 import aumentar, diminuir, dobrar, metade, moeda
v = bool
p = float(input("Digite o preço do produto R$"))
while True:
    r = input("Deseja ver os valores formatados? [1 SIM / 0 NÃO] ")[0]
    if r in ("1", "0"):
        if r == "0":
            v = False
        break

print(f"""A metade do preço {moeda(p, v)} ==> R${moeda(metade(p), v)}
O dobro do preço {moeda(p, v)} ==> R${moeda(dobrar(p), v)}
O preço {moeda(p, v)} aumentado em 15% ==> {moeda(aumentar(p, 15), v)}
O preço {moeda(p, v)} diminuído em 15% ==> {moeda(diminuir(p, 15), v)}""")