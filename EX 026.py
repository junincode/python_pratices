f = input("Digite um frase: ")
f = f.replace(" ", "")
print("A letra 'a' aparece {} vezes.".format((f.upper().count('A'))))
print("A letra 'a' aparece pela primeira vez na {}° posição".format((f.upper().find('A')+1)))
print("A letra 'a' aparece pela última vez na {}° posição".format((f.upper().rfind('A')+1)))