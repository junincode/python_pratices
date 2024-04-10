f = input("Digite uma frase: ")
f = f.strip()
f = f.capitalize()
f = f.replace(" ", "")
v = "Santo" in f[0:6]
print("Começa com a palavra 'Santo'? {}".format(v))

