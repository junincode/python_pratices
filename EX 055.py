mai = 0
men = 0
pesos = []
for c in range(1,6):
    p = float(input("[{}]Digite seu peso: Kg".format(c)))
    pesos.insert(c, p)
    if c == 1:
        mai = p
        men = p
    else:
        if p > mai:
            mai = p
        if p < men:
            men = p
print('''
==================================
       Pesos registrados:
{}
==================================
MENOR PESO: {}
MAIOR PESO: {}'''.format(pesos, men, mai))
