"""
Autor: Moises Auad Werneck
Descrição: Calcula a exponenciação modular de a^b mod n
Entrada: 3 números inteiros
Saída: O módulo de a^b por n
"""

def expmod(a, b, n):
    if b == 0:
        return 1
    elif b%2 == 1:
        r = a * expmod(a, b-1, n) % n

    elif b%2 == 0:
        r = pow(expmod(a, b/2, n), 2) % n
    
    return r

print(expmod(int(input("Digite <a> ")), int(input("Digite <b> ")) , int(input("Digite <n> "))))
