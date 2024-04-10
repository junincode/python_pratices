from datetime import date
print("\033[1;32m-=-\033[m"*12)
print("{:^36}".format("EXÉRCITO"))
print("\033[1;32m-=-\033[m"*12)
atual = date.today().year
a = int(input("Ano de nascimento: "))
if (atual - a) < 18:
    print("Você ainda vai se alistar daqui a {} ano(s).".format(18-(atual-a)))
elif (atual - a) == 18:
    print("Você está na idade de se alistar ao exército.")
else:
    print("Você já se alistou ou deveria ter se alistado há {} ano(s).".format((atual-a)-18))