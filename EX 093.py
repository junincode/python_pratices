dados, gols = dict(), list()
tg = 0
dados["Nome"] = str(input("Nome do jogador: ")).strip()
dados["Número de partidas"] = int(input("N° de partidas jogadas: "))
for i in range(0, dados["Número de partidas"]):
    gols.append(int(input((f"Gols no {i+1}° jogo: "))))
    tg += gols[i]
dados["Gols"] = gols
dados["Aproveitamento"] = F"{tg/dados["Número de partidas"]:.2f} gols por partida"
dados["Total de gols"] = tg
print(dados)
print("=-"*20)
for k, v in dados.items():
    if k == "Gols":
        print(f"O jogador {dados["Nome"]} jogou {dados["Número de partidas"]} partidas.")
        print("=-"*20)
        for i, c in enumerate(gols):
            print(f"   {i+1}a Partida : {c} Gol(s)")
    print(f"{k} = {v}")


