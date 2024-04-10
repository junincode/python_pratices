mv, m, lm = 0, 0, []
ln, ls, li = [], [], []
for c in range(1,5):
    n = input("[{}] Digite seu nome: ".format(c))
    s = input("[{}] Digite seu Sexo (M/F): ".format(c))
    i = int(input("[{}] Digite sua idade: ".format(c)))
    print("="*20)
    m += i
    ln.insert(c, n)
    ls.insert(c, s)
    li.insert(c, i)
    if i > mv and s.upper() == "M":
        nmv = n
    if i == mv:
        nmv = "Mais de 1 homem possui {} anos".format(i)
    if i > mv:
        mv = i
    if s.upper() == "F" and i < 20:
        lm.insert(0, n)
m /= 4
print("RELATÓRIO:")
for c in range(1,5):
    print(''' {}° NOME: {}
    SEXO: {}
    IDADE: {}
    ======================='''.format(c, ln[c-1],ls[c-1], li[c-1]))
print("A média das idade registradas é: {:.2f} anos".format(m))
print("O Homem mais velho é {}".format(nmv))
print("{} mulher(es) tem menos de 20 anos: {}".format(len(lm),lm))


'''print("{}° NOME: {}".format(c, ln[c-1]))
        print("SEXO: {}".format(ls[c-1]))
        print("IDADE: {}".format(li[c-1]))
        print("="*20)'''

