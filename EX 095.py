lista, dados, gols = list(), dict(), list()
tg, r, cod, e = 0, " ", 0, 0
while r not in "Nn":
    dados["Cod"] = cod
    dados["Nome"] = str(input("Nome do jogador: "))
    dados["Número de partidas"] = int(input("N° de partidas jogadas: "))
    for i in range(0, dados["Número de partidas"]):
        gols.append(int(input(f"Gols no {i+1}° jogo: ")))
        dados["Total de gols"] += gols[i]
    dados["Gols"] = gols[:]
    dados["Aproveitamento"] = F"{tg/dados["Número de partidas"]:.2f} gols por partida"
    gols.clear()
    tg = 0
    r = str(input("Deseja continuar [S/N]? "))
    while r not in "SsNn":
        r = str(input("RESPOSTA INVÁLIDA. Deseja continuar [S/N]? "))
    lista.append(dados.copy())
    cod += 1
print("=-"*25)
print(f"{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}")
print("-"*50)
for i, c in enumerate(lista):
    print(f"{c["Cod"]:<4}{c["Nome"]:<15}{str(c["Gols"]):<20}{c["Total de gols"]:<5}")
print("-"*50)
while True:
    e = int(input("Deseja analisar qual jogador? [999 PARA PARAR]"))
    if e == 999:
        break
    else:
        while not 0 <= e < cod:
            e = int(input("RESPOSTA INVÁLIDA. Deseja analisar qual jogador? "))
    print("=-"*25)
    print(f"{F"LEVANTAMENTO DO JOGADOR {lista[e]["Nome"]}":^20}")
    for i, k in enumerate(lista[e]["Gols"]):
        print(f"    {i+1}° Partida ==> {k} gol(s).")
    print(f"Com aproveitamento de {lista[e]["Aproveitamento"]}")
    print("=-"*25)
print("<< FIM DA ANÁLISE >>")
