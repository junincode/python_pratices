from EX111.UTILIDADE_CEV.MOEDA107 import aumentar, diminuir, dobrar, metade
p = float(input("Digite o preço do produto R$"))
print(f"""A metade do preço R${p} ==> R${metade(p)}
O dobro do preço R${p} ==> R${dobrar(p)}
O preço aumentado em 15% é {aumentar(p)}
O preço diminuído em 15% é {diminuir(p)}""")