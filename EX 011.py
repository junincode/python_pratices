l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))
m = l*a//2
if (l*a)%2 == 1:
    m = m + 1
else:
    m = m
print("A área da parede é {} e serão necessários {} baldes para pintar.".format(l*a, m))