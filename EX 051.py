print("="*20)
print("{:^20}".format("GERADOR DE PA"))
print("="*20)
n = int(input("Digite o 1° termo: "))
r = int(input("Digite a razão da PA: "))
x = int(input("Quanto termos você deseja ver? "))
for c in range(1,x+1):
    print(n, end= " -> ")
    n += r
print("ACABOU")