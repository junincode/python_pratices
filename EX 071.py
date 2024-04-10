n100, n50, n20, n10, n1 = 0, 0, 0, 0, 0
print('''{}
{:^20}
{}'''.format("="*20, "CAIXA ELETRÔNICO", "="*20))
v = float(input("Digite o valor a ser sacado R$"))
while v >= 100:
    n100 += 1
    v -= 100
while v >= 50:
    n50 += 1
    v -= 50
while v >= 20:
    n20 += 1
    v -= 20
while v >= 10:
    n10 += 1
    v -= 10
while v >= 1:
    n1 += 1
    v -= 1
print('''O VALOR DE R${} FOI SACADO EM: 
''')
if n100 != 0:
    print(f"{n100} NOTAS DE R$100")
if n50 != 0:
    print(f"{n50} NOTAS DE R$50")
if n20 != 0:
    print("{} NOTAS DE R$20".format(n20))
if n10 != 0:
    print("{} NOTAS DE R$10".format(n10))
if n1 != 0:
    print("{} MOEDAS DE R$1".format(n1))