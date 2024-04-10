s = " "
while s not in "FfMm":
    s = input("Digite seu sexo [F/M]:  ", ).strip()
    if s not in "FfMm":
        print('''ERROR.
[TENTE NOVAMENTE] ''', end= "")
if s in "Ff":
    print("SEXO FEMININO REGISTRADO.")
else:
    print("SEXO MASCULINO REGISTRADO.")

