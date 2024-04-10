v = float(input("Qual o valor do produto? R$"))
print("[1] À vista em dinheiro")
print("[2] À vista no cartão")
print("[3] Em 2x no cartão")
print("[4] Em 3 vezes ou mais")
f = int(input("Qual a forma de pagamento?"))
print("="*15)
if f == 1:
    print("O pagamento em dinheiro ficou em R${}".format(v))
elif f == 2:
    print("5% de DESCONTO!")
    print("O pagamento à vista no cartão ficou em R${:.2f}".format(v*0.95))
elif f == 3:
    print("O pagamento no cartão ficou em 2x de R${:.2f}".format(v/2))
elif f == 4:
    v = v * 1.2
    np = int(input("Em quantas parcelas? [3--24]"))
    if  3 <= np <= 24:
        print("Pagamento com 20% de juros aprovado em {}x de R${:.2f}".format(np, v/np))
        print("O valor total ficou em R${:.2f}".format(v))
    elif np > 24:
        print("O número de parcelas requisitado excede nosso limite.")
    else:
        print("O número de parcelas é muito pequeno.")
else:
    print("OPÇÃO INVÁLIDA. Tente novamente.")
