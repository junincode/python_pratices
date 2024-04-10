dados, notas, lista = list(), list(), list()
r, f = " ", 0
while r not in "Nn":
    dados.append(str(input("NOME: ")))
    notas.append(float(input("1a NOTA: ")))
    notas.append(float(input("2a NOTA: ")))
    dados.append(notas[:])
    dados.append((notas[0] + notas[1])/2)
    lista.append(dados[:])
    notas.clear()
    dados.clear()
    r = str(input("DESEJA CONTINUAR? [S/N] "))
    while r not in "SnNn":
        r = str(input("RESPOSTA INVÁLIDA. DESEJA CONTINUAR? [S/N] "))
print(lista)
print("=-"*20)
print("DADOS CADASTRADOS: ")
print("=-"*20)
i = 0
for c in lista:
    i += 1
    print(f"ALUNO {i}")
    print(F"NOME: {c[0]}")
    print(F"MÉDIA: {c[2]:.2f}")
    print("=-"*20)
while f != 999:
    for i, c in enumerate(lista):
        print(f"{i} - {c[0]}")
    f = int(input("DESEJA VER AS NOTAS DE QUAL ALUNO? [999 INTERROMPE]. "))
    if f == 999:
        break
    else:
        while not 0 <= f <= len(lista)-1:
            f = int(input("ERRO. DESEJA VER AS NOTAS DE QUAL ALUNO? [999 INTERROMPE]. "))
    print(f"ALUNO {lista[f][0]} / NOTAS: {lista[f][1]}")
    print("=-"*20)
print("SISTEMA ENCERRADO.")