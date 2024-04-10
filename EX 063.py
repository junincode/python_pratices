c, f, fibo = 1, 1, [0]
n = int(input("Quantos termos Fibonacci deseja ver? "))
print("{}-->".format(fibo[0]), end= "")
while c != n:
    print("{}-->".format(f), end= "")
    fibo.insert(c, f)
    f += (fibo[c-1])
    c += 1
print("FIM")