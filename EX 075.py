n = (int(input("Digite um número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")))
print(f"O valor 9 apareceu {n.count(9)} vezes")
print(f"O valor 3 apareceu primero na posição {n.index(3)}" if n.index(3) in (0, 1, 2, 3) else "O valor 3 não apareceu.")
print(f"Os valores paras foram: ", end= "")
for i in range(0,4):
    if n[i]%2 == 0:
        print(n[i], end=" ")