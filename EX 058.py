from random import randint
e = randint(0, 10)
r, t = 0, 0
print("="*20)
print("{:^20}".format("ADVINHAÇÃO"))
print("="*20)
print("Pensei em um número de 0 a 10, tente advinhar.")
while r != e:
    while r not in (0,1,2,3,4,5,6,7,8,9,10):
        r = int(input("ERROR. Digite um valor: ".format(r)))
    if t == 0:
        r = int(input("Digite um valor: ".format(r)))
    elif r > e:
        r = int(input("MENOS... Digite um valor: ".format(r)))
    elif r < e:
        r = int(input("MAIS... Digite um valor: ".format(r)))
    t += 1
print("Acertou! O computador pensou no número {} e você advinhou com {} tentativa(s).".format(e, t))

