n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
print("A média das notas {:.2f} e {:.2f} é {:.2f}".format(n1, n2, (n1 + n2)/2))
m = (n1 + n2)/2
if m >= 8:
    A = "A"
elif m >= 6:
    A = "B"
elif m >= 5:
    A = "C"
elif m >= 3:
    A = "D"
elif m >= 3:
    A = "E"
else:
    A = "F"
print("Você atingiu o Ranking {}".format(A))
