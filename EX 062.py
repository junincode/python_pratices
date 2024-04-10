t = int(input("Digite o 1° termo: "))
r = int(input("Digite a razão da PA: "))
qt = int(input("Quantos termos quer ver? "))
c = 1
while c != qt + 1:
    print("{}-->".format(t), end="")
    t += r
    c += 1
print("...")