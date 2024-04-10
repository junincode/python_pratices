import pandas as pd
import datetime
i = 1
estudantes_da_escola = dict() # usada para separar linhas de jogadores de mesma escola
estudantes_e_escolas = dict() # usada para organizar cada escola com seus jogadores em um dicionário
Data = pd.read_csv("C:/Users/mauad/Downloads/Players.csv")
pd.DataFrame(Data)
Data["Player"].fillna(value= "X", inplace=True)
print(Data.loc[0, :])
print()
estudantes_de_indiana = Data.loc[Data["collage"] == "Indiana University"]
estudantes_de_indiana = list(estudantes_de_indiana.iloc[:, 1])
all_schools = Data["collage"].unique()

#Separando Jogadores por universidades de origem
for school in all_schools:
    estudantes_da_escola = Data.loc[Data["collage"] == f"{school}"]
    estudantes_da_escola = list(estudantes_da_escola.loc[:, "Player"])
    estudantes_e_escolas[f"{school}"] = estudantes_da_escola

for k, v in estudantes_e_escolas.items(): #demonstração de jogadores separados por universidade
    print(f"ESTUDANTES DE {k}: {v}")

print("Os 20 maiores jogadores registrados!")
print("=-"*20)
# definindo a lista com os 20 maiores jogadores da base de dados.
top20_altura = Data[["Player","height"]].sort_values(by="height", ascending=False).head(20)
for k, v in top20_altura.loc[:,"Player"].items():
    print(f"Em {i}° Lugar: {v}", end="")
    print(f"Com {top20_altura.loc[k, "height"]/100}m")
    i += 1

#Definindo os 20 mais novos jogadores da base de dados.
top_20_mais_novos = Data.loc[:, ["Player", "born"]].sort_values(by= "born", ascending=False).head(20)
i = 1
print("Os 20 mais novos")
print("=-"*20)
for k, v in top_20_mais_novos.loc[:, "Player"].items():
    print(f"Em {i}° Lugar: {v} com {datetime.date.today().year - top_20_mais_novos.loc[k, "born"]} anos.")
    i += 1

top_20_mais_pesados = Data.loc[:, ["Player", "weight"]].sort_values(by= "weight", ascending= False).head(20)
i = 1

print("=-"*20)
print("Os 20 mais pesados registrados.")
print("=-"*20)
for k, v in top_20_mais_pesados.loc[:, "Player"].items():
    print(f"Em {i}° Lugar: {v} com {top_20_mais_pesados.loc[k, "weight"]} Kg")
    i += 1
print("=-"*20)

#Encontrando Coincidências nas 3 listas [Novos, Altos e Pesados]
coincidencia, cPA, cNP, cNA = list(), list(), list(), list()

for n_altura in top20_altura["Player"]:
    for n_novo in top_20_mais_novos["Player"]:
        for n_pesado in top_20_mais_pesados["Player"]:
            if n_pesado == n_novo:
                cNP.append(n_novo)
            elif n_pesado == n_altura:
                cPA.append(n_pesado)
            elif n_novo == n_altura:
                cNA.append(n_altura)
            elif n_pesado == n_novo == n_altura:
                coincidencia.append(n_pesado)

"""
print("Lista dos inclusos nas 3 listas:")

for nome in coincidencia:
    print(nome)

print("Novo e Alto")
print(list(set(cNA)))

print()
print("Novo e Pesado")
print(list(set(cNP)))

print()
print("Alto e Pesado")
print(list(set(cPA)))
"""

while True:
    nome = str(input("Qual jogador quer pesquisar? aperte ENTER para SAIR.")).strip().title()
    if nome == "":
        break
    for k, v in estudantes_e_escolas.items():
        if nome in v:
            print("=-"*20)
            print(f"{nome} é da universidade {k}")
    for n in Data.iloc[:, 0]:
        i = 1
        if nome == Data.loc[n, "Player"]:
            i = 0
            print(f"Seu peso é {Data.loc[n, "weight"]} Kg.")
            print(f"Sua altura é {Data.loc[n, "height"]/100}m.")
            print(f"Nasceu em {int(Data.loc[n, "born"])} na cidade de {Data.loc[n, "birth_city"]}.")
            print(f"Possui atualmente {datetime.date.today().year - Data.loc[n, "born"]} anos.")
            print("=-"*20)
    if i != 0:
        print("Jogador não encontrado.")
print("Saindo...")



