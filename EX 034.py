print("="*30)
print("{:^30}".format("Quadro de aumentos"))
print("="*30)
s = float(input("Digite o salário do funcionários: R$"))
if s <= 1250:
    ns = s*115/100
    print("Com o aumento de 15%, o novo salário é R$z{}".format(ns))
else:
    ns = s * 110/100
    print("Com o aumento de 10%, o novo salário é R${}".format(ns))
