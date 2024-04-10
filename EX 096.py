def Area(X, Y):
        A = X*Y
        print(f"A área das dimensões {X}m X {Y}m é {A:.2f}m²")


a = float(input("Digite a dimensão do comprimento: "))
b = float(input("Digite a dimensão da largura: "))
Area(a, b)