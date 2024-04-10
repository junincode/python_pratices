import random
print("Eu escolhi um número de 1 a 5.")
a = int(input("Sua aposta: "))
s = [1,2,3,4,5]
s = random.choice(s)
print("YES! eu escolhi o número {} mesmo!".format(s) if a == s else "Eu escolhi o n°{}, Tente novamente.".format(s))