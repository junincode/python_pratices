l1 = float(input("PRIMEIRO LADO: "))
l2 = float(input("SEGUNDO LADO: "))
l3 = float(input("TERCEIRO LADO: "))
if l1 != l2 and l2 != l3 and l1 != l3:
    t = "ESCALENO"
elif (l1 == l2 or l3 == l2 or l3 == l1) and not(l1 == l2 == l3):
    t = "ISÓSCELES"
else:
    t = "EQUILÁTERO"
print("O triângulo com lados {}, {} e {} é {}".format(l1, l2, l3, t))