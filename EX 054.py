men = []
mai = []
from datetime import date
for c in range(1,8):
    a = int(input("[{}] Digite seu ano de nacimento: ".format(c)))
    if date.today().year - a < 21:
        men.insert(0,a)
    else:
        mai.insert(0,a)
print("Dos listados acima:")
print("{} menor(es) de idade: {}".format(len(men), men))
print("{} maior(es) de idade: {}".format(len(mai), mai))