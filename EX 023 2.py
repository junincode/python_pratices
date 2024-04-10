import math
n = int(input("Digite um número de 0 a 9999: "))
um = n//1000
c = n//100 - um*10
d = n//10 - um*100 - c*10
d = d.__floor__()
u = n - um*1000 - c*100 - d*10
print("O número contém: ")
print("{} UNIDADES".format(u))
print("{} DEZENAS".format(d))
print("{} CENTENAS".format(c))
print("{} UNIDADES DE MILHAR".format(um))
