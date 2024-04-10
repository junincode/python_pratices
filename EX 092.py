import datetime
ttr, at, ia, aa = 0, 0, 0, 0
p = dict()
p["NOME"] = str(input("NOME: "))
p["NASCIMENTO"] = int(input("ANO DE NASCIMENTO: "))
i = datetime.datetime.today().year - p["NASCIMENTO"]
p["CLT"] = int(input("N° DA CLT [0 CASO NÃO TENHA]: "))
if p["CLT"] == 0:
    p["CLT"] = "Não possui."
    p["IDADE"] = i
elif p["CLT"] != 0:
    p["ANO DA CONTRATAÇÃO"] = int(input("ANO DA CONTRATAÇÃO: "))
    p["SALARIO R$"] = float(input("SALÁRIO ATUAL: R$"))
    at = datetime.datetime.today().year - p["ANO DA CONTRATAÇÃO"]
    p["ANOS DE TRABALHO RESTANTES"] = 35 - at
    p["IDADE DE APOSENTADORIA"] = i + ttr
    p["ANO DE APOSENTADORIA"] = datetime.datetime.today().year + ttr
    p["IDADE"] = i
print("=-"*20)
for k, v in p.items():
    print(f"{k} {v}")
