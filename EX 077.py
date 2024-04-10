z = 0
t = ("ENQUANTO", "AINDA", "PRECISO", "IMPORTA", "AJUDA", "CRESCIMENTO", "GRATIDÃO", "DOMINO", "COLCHAO")
for i in range(0,len(t)):
    print(f"\nA palavra {t[i]} tem as vogais: ",end="")
    for c in range(0, len(t[i])):
        if t[i][c] in "aeiouAEIOU":
            if str(t[i]).count(str(t[i][c])) > 1:
                if z == 0:
                    z += 1
                    print(t[i][c], end=" ")
                else:
                    t = t
            else:
                print(t[i][c], end=" ")
    z = 0