n = int(input("Digite um número de 0 a 9999: "))
u = n % 10
d = (n % 100 )//10
c = (n % 1000 )//100
m = (n % 10000 )//1000
print("O número contém: ")
print("{} UNIDADES".format(u))
print("{} DEZENAS".format(d))
print("{} CENTENAS".format(c))
print("{} UNIDADES DE MILHAR".format(m))

