n, par, impar = [], [], []
for i in range(0,10):
    n.append(int(input(f"{i+1}-Digite um número: ")))
for i in range(0,10):
    if n[i]%2 == 0:
        par.append(n[i])
    else:
        impar.append(n[i])
print(f"""================================
O conjunto de pares digitados foi {par}
O conjunto de ímpares digitados foi {impar} 
Todos os valores: {n}""")