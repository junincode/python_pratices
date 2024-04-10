r, n, n5, p5 = " ", [], 0, []
while r not in "Nn":
    n.append(int(input("Digite um número: ")))
    r = input("Deseja Continuar? [S/N] ")
    if n[-1] == 5:
        n5 += 1
        p5.append(n.index(5))
    while r not in "SsNn":
        r = input("RESPOSTA INVÁLIDA! Deseja Continuar? [S/N] ")
n.sort(reverse=True)
print(f'''Ao todo, foram digitados {len(n)} valores.
Em ordem decrescente: {n}''')
print(f"O número 5 não apareceu." if n5 == 0 else f"O número 5 apareceu {n5} vezes nas posições {p5}")