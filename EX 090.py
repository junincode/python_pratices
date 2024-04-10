a = dict()
a["Nome"] = str(input("NOME DO ALUNO: "))
a["Média"] = float(input("MÉDIA DO ALUNO: "))
if a["Média"] >= 7:
    a["Situação"] = "APROVADO"
else:
    a["Situação"] = "REPROVADO"
print("=-"*20)
for i, k in a.items():
    print(f"{i}: {k}")
