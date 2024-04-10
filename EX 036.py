print("\033[1;35m=\033[m"*30)
print("{:^40}".format("\033[1;35mBANCO\033[m"))
print("\033[1;35m=\033[m"*30)
s = float(input("Qual o salário do devedor? R$"))
v = float(input("Qual o valor da casa? R$"))
a = int(input("Em quantos anos a casa será paga? "))
if v/(a*12) <= 0.30*s:
    print("O empréstimo foi aprovado em {} parcelas de R${:.2f}".format(a*12,v/(a*12)))
else:
    print("A parcela {:.2f} excede 30% do salário: Empréstimo negado.".format(v/(a*12)))