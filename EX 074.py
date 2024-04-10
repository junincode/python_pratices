import random
mai, men = 0, 0
n = (random.randint(1, 10),
     random.randint(1, 10),
     random.randint(1, 10),
     random.randint(1, 10),
     random.randint(1, 10)
     )
for i in range(0,5):
    print(n[i], end=" ")
for c in range(0,5):
    if c == 0:
        mai = n[c]
        men = n[c]
    if n[c] > mai:
        mai = n[c]
    elif n[c] < men:
        men = n[c]
print(F'''
O MENOR É {men}
O MAIOR É {mai}''')