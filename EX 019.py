import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno ")
a4 = input("Último aluno: ")
a = [a1, a2, a3, a4]
e = random.choice(a)
print("O aluno(a) escolhido(a) foi {}".format(e))