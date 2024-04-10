f = input("Escreva uma frase: ")
f = f.strip()

print("As 10 primeiras letras da sua frase são: '{}' ".format(f[:11]))
print("A sua frase contém {} letras".format(len(f) - f.count(" ")))
print("A sua frase contém {} palavras.".format(len(f.split())))
print("O primeiro nome possui {} letras.".format(len((f.split()[0]))))
print("A sua frase em MAIÚSCULAS é: {}".format(f.upper()))
print("A sua frase contém {} espaços".format(f.count(" ")))
