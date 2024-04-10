kg = float(input("Qual a sua massa total? [Kg]"))
alt = float(input("Qual a sua altura? [m]"))
imc = kg / (pow(alt,2))
print("O seu IMC é {:.2f}".format(imc))
if imc <= 18.5:
    print("Você está ABAIXO DO PESO.")
elif 18.5 < imc <= 25:
    print("Você está no PESO IDEAL.")
elif 25 < imc <= 30:
    print("Você está com SOBREPESO.")
elif 30 < imc <= 40:
    print("Você está com OBESIDADE.")
else:
    print("Você está com OBESIDADE MÓRBIDA.")
