n1 = float(input("Primeiro lado do triângulo: "))
n2 = float(input("Segundo lado do triângulo: "))
n3 = float(input("Terceiro lado do triângulo: "))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print("Os segmentos PODEM formar um triângulo!")
    if (n1 == n2 or n2 == n3 or n1 == n3) and not (n1 == n2 == n3):
        print("O triângulo é ISÓSCELES!")
    elif n1 != n2 and n1 != n3 and n3 != n2:
        print("O triângulo é ESCALENO!")
    else:
        print("O triângulo é EQUILÁTERO!")
else:
    print("Os segmentos NÃO PODEM formar um triângulo.")