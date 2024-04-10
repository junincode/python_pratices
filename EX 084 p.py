dados, i = [], 1
pessoas = []
r = " "
while r not in "Nn":
    print(f"{i} << CADASTRO >>")
    dados.append(str(input("NOME: ")))
    dados.append(int(input("IDADE: ")))
    dados.append(str(input("SEXO [F/M] ")))
    while dados[2] not in "FfmM":
        del dados[2]
        dados.append(str(input("RESPOSTA INVÁLIDA. SEXO [F/M] ")))
    pessoas.append(dados)
    dados = []
    r = input("DESEJA CONTNINUAR? [S/N] ")
    i += 1
    while r not in "SsNn":
        r = input("RESPOSTA INVÁLIDA. DESEJA CONTINUAR? [S/N] ")
for z, c in enumerate(pessoas):
    print(f"{z+1}a PESSOA.")
    print(f"Nome: {c[0]}")
    print(f"Idade: {c[1]}")
    print(f"Sexo: {c[2]}")
    print("=-"*20)

