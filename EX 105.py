def notas(*num, sit=False):
    s = 0
    lista = dict()
    lista["Notas"] = len(num)
    for i, c in enumerate(num):
        if i == 0:
            lista["Maior"] = c
            lista["Menor"] = c
        elif c > lista["Maior"]:
            lista["Maior"] = c
        elif c < lista["Menor"]:
            lista["Menor"] = c
        s += c
    lista["Média"] = s / lista["Notas"]
    if sit:
        if lista["Média"] > 8:
            lista["Situação"] = "ÓTIMA"
        elif 6 < lista["Média"] <= 8:
            lista["Situação"] = "BOA"
        elif 5 < lista["Média"] <= 6:
            lista["Situação"] = "OK"
        else:
            lista["Situação"] = "PRECÁRIA"
    print(lista, end=" ")


notas(4.5, 4, 10, 9, 6, 10, sit=True)







