n = list()
for i in range(0,6):
    n.append(int(input(f"{i+1}-Digite um número: ")))
    while n.count(n[i]) > 1:
        del n[i]
        n.append(int(input(f"Número já cadastrado! {i+1}-Digite outro número: ")))
print(sorted(n))
