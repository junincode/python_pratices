def ficha(n="<desconhecido>", g=0):
    print("=-"*20)
    if n == "":
        n = "<desconhecido>"
    if g == "":
        g = 0
    print(f"""Nome do Jogador: {n}
N° de Gols: {g}
{"=-"*20}""")


nome = (input("Cadastre o nome do jogador: "))
gols = (input("Digite o número de gols: "))
print("PRIMEIRA FICHA")
ficha(nome, gols)
print("SEGUNDA FICHA")
ficha()