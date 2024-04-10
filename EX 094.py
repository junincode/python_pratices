pessoa, lista, m, pam, am = dict(), list(), list(), list(), dict()
r, i, si, z = " ", 0, 0, 0
while r not in "Nn":
    pessoa["Nome"] = str(input("NOME: "))
    pessoa["Idade"] = int(input("IDADE: "))
    pessoa["Sexo"] = str(input("SEXO [M/F]: "))
    while pessoa["Sexo"] not in "FfMm":
        pessoa["Sexo"] = str(input("RESPOSTA INVÁLIDA. SEXO [M/F]: "))
    lista.append(pessoa.copy())
    if pessoa["Sexo"] in "Ff":
        m.append(pessoa["Nome"])
    si += pessoa["Idade"]
    i += 1
    r = str(input("Deseja continuar [S/N]? "))
    while r not in "SsNn":
        r = str(input("RESPOSTA INVÁLIDA. Deseja continuar [S/N]? "))
    print("=-"*20)
mi = si/i
print(lista)
print("=-"*25)
for c in lista:
    z += 1
    print(f"{z}a PESSOA", end=" > ")
    for k, v in c.items():
        print(f"{k} = {v}", end=" ")
    print()
for c in lista:
    for k, v in c.items():
        if k == "Idade":
            if v > mi:
                am.clear()
                am["Nome"] = c["Nome"]
                am["Idade"] = c["Idade"]
                pam.append(am.copy())
print(F"""FORAM CADASTRADAS AO TODO {i} PESSOA(S)
A MÉDIA DAS IDADES FOI {mi:.1f} ANOS
AS MULHERES CADASTRADAS SÃO {m}
AS PESSOAS ACIMA DA MÉDIA DE IDADE ({mi:.1f}) SÃO:""")
for i in pam:
    for k, v in i.items():
        if k == "Nome":
            print(f"{v}", end=" ")
        elif k == "Idade":
            print(f"com {v} anos.")
