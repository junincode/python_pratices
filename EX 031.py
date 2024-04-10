print("="*20)
print("{:^20}".format("BILHETERIA"))
print("="*20)
k = float(input("Quanto KM tem trajeto? "))
if k <= 200:
    p = k * 0.5
    print("Viagem comum, o preço é R${:.2f}".format(p))
else:
    p = k*45/100
    print("Viagem longa, o preço é R${:.2f}".format(p))

