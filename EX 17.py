from math import sqrt, pow
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = sqrt(pow(co, 2) + pow(ca, 2))
print("A hipotenusa vale {:.2f}".format(h))