print("="*20)
print("Radar")
print("="*20)
v = float(input("Qual a velocidade do carro? Km/h "))
if v <= 80:
    print("Velocidade permitida. Sem penalidades.")
else:
    print("Velocidade acima do limite (80), multa de R${:.2f}".format((v-80)*7))