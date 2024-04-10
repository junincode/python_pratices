d = 0
ld = []
n = int(input("Digite um número: "))
for c in range(1, n+1):
    if n%c==0:
        d += 1
        ld.insert(0,c)
        print("\033[1;34m{}\033[m".format(c), end= ' ')
    else:
        print(c, end=" ")
if d == 2:
    print('''
O número {} é PRIMO! Isto é, possui apenas 2 divisores[{} e 1].'''.format(n,n))
elif d > 2:
    print('''
O número {} não é primo!, já que {} são todos os seus divisores.'''.format(n, ld))
else:
    print('''
O número 1 não é primo''')