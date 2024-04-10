from EX111.UTILIDADE_CEV.MOEDA107 import aumentar, diminuir, dobrar, metade, moeda
p = float(input("Digite o preço do produto R$"))
print(f"""A metade do preço {moeda(p)} ==> R${moeda(metade(p))}
O dobro do preço {moeda(p)} ==> R${moeda(dobrar(p))}
O preço {moeda(p)} aumentado em 15% ==> {moeda(aumentar(p))}
O preço {moeda(p)} diminuído em 15% ==> {moeda(diminuir(p))}""")