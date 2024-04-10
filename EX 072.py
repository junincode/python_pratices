n = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze","doze", "catorze",
"quinze", "dezesseis", "dezessete", "dezoito", "dezonove", "vinte")
v = int(input("Digite um número de 0 a 20: "))
while not (0 <= v <= 20):
    v = int(input("RESPOSTA INVÁLIDA. Digite um número de 0 a 20: "))
print(f"O número {v} é, por extenso, {n[v]}")

