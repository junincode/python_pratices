def expmod(a, b, n):
    if b == 0:
        return 1
    elif b%2 == 1:
        r = a * expmod(a, b-1, n) % n
        print("mul")

    elif b%2 == 0:
        r = pow(expmod(a, b/2, n), 2) % n
        print("pow")
    return r

print(expmod(51, 49, 19))