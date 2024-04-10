from time import sleep
e = str(input("Digite sua expressão númerica: "))
e = e.replace("", " ")
e = e.split()
z = e
if e[0] == ")" or e[-1] == "(":
    print("Ajustando sua expressão...")
    sleep(1.5)
    while e[0] == ")":
        del e[0]
    while e[-1] == "(":
        del e[-1]
    print("".join(e))
if e.count(("(")) != 0 and e.count(")") != 0:
    for i, c in enumerate(e):
        if e[i] == "(":
            del e[i]
            del e[e.index(")")]
if e.count("(") != e.count(")"):
    v = "INVÁLIDA"
    if e.count(("(")) > e.count((")")):
        m = "Faltou parênteses à direita."
        for i, c in enumerate(e):
            if c == "(":
                print(f"\033[1;31m{c}\033[m", end="")
            else:
                print(c, end="")
    else:
        for i, c in enumerate(e):
            if c == ")":
                print(f"\033[1;31m{c}\033[m", end="")
            else:
                print(c, end="")
        m = "Faltou parênteses à esquerda."
elif e.count("(") + e.count((")")) == 0:
    v = "VÁLIDA"
    m = "Não há parênteses para analisar."
else:
    v = "VÁLIDA"
    m = f"Os pares de parênteses estão devidamente posicionados."
print('''
==============================''')
print(f"Sua expressão está {v}")
print(f"MOTIVO: {m}")