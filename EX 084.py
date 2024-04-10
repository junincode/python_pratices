dados, pessoas = list(), list()
r = " "
i, mp, ml = 0, list() , list()
while r not in "Nn":
    i += 1
    print(f"{i}a PESSOA.")
    dados.append(str(input("NOME: ")))
    dados.append(float(input("PESO[Kg]: ")))
    pessoas.append(dados[:])
    if dados[1] >= 90:
        mp.append(dados[:])
    if dados[1] <= 70:
        ml.append(dados[:])
    dados.clear()
    r = input("DESEJA CONTINUAR? [S/N] ")
    while r not in "SsNn":
        r = input("RESPOSTA INVÁLIDA. DESEJA CONTINUAR? [S/N] ")
print(f"Ao total foram cadastradas {i} pessoas.")
for i, c in enumerate(pessoas):
    print(F"{i+1}a PESSOA =========")
    print(f"NOME: {c[0]}")
    print(f"PESO: {c[1]}Kg")
if len(ml) >= 1:
    print("="*20)
    print("PESSOAS MAIS LEVES:")
    for i in mp:
        print(F"NOME: {i[0]}")
if len(mp) >= 1:
    print("="*20)
    print("PESSOAS MAIS PESADAS:")
    for i in ml:
        print(F"NOME: {i[0]}")