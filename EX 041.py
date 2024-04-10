print("="*20)
print("{:^20}".format("CONFEDERAÇÃO"))
print("="*20)
i = int(input("Idade do atleta: "))
if i <= 9:
    c = "\033[1;34mMIRIM\033[m"
elif i <= 14:
    c = "\033[1;33mINFANTIL\033[m"
elif i <= 19:
    c = "\033[1;32mJUVENIL\033[m"
elif i == 20:
    c = "\033[1;31mSÊNIOR\033[m"
else:
    c = "\033[1;35mMASTER\033[m"
print("O atleta de {} anos pertence à categoria {}".format(i, c))