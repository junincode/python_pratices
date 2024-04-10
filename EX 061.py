t = int(input("Digite o 1° termo: "))
r = int(input("Digite a razão da PA: "))
qt = int(input("Quantos termos quer ver? "))
c = 1
qtt = 0
res = " "
while res not in "Nn":
    if c != 1:
        qt = int(input("Deseja ver mais quantos termos? "))
        c = 1
    while c != qt+1:
        print("{}-->".format(t), end="")
        t += r
        c += 1
        qtt += 1
    print("...")
    res = input('''
Deseja continuar?''')
print("="*15)
print("FORAM DIGITADOS AO TOTAL {} TERMOS.".format(qtt))
print("FIM.")
