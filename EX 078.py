n, mai, men, pmai, pmen = list(), 0, 0, 0, 0
for i in range(0, 5):
    n.insert(i, int(input(f"Digite o {i+1}° número.")))
    if i == 0:
        mai = n[i]
        men = n[i]
    else:
        if n[i] < men:
            men = n[i]
            pmen = i
        elif n[i] > mai:
            mai = n[i]
            pmai = i
print(n)
print(f"""O maior valor é {mai} na posição {pmai} 
e o menor é {men} na posição {pmen}""")