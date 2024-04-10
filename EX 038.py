n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    maior = n1
    menor = n2
    print("Maior: {}".format(maior))
    print("Menor: {}".format(menor))
elif n2 > n1:
    maior = n2
    menor = n1
    print("Maior: {}".format(maior))
    print("Menor: {}".format(menor))
else:
    print("Os número digitados são iguais.")
