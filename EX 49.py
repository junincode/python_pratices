print("="*20)
print("{:^20}".format("TABUADA"))
print("="*20)
n = int(input("De qual número você deseja ver a tabuada?"))
for c in range(1,11):
    print("{} X {} = {}".format(n, c, n*c))
print("{}{}{}".format("="*5, "FIM", "="*5))
