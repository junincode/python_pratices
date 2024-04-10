print("\033[1;32m-=-\033[m"*12)
print("{:^36}".format("ESCOLA"))
print("\033[1;32m-=-\033[m"*12)
n1 = float(input("Primera nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2)/2
print("======{}======".format(" RESULTADO "))
print("Com a média {}".format(m))
if m > 7:
    print("Você já está \033[1;32mAPROVADO\033[m!")
elif 5 <= m < 7:
    print("Você está em \033[1;33mRECUPERAÇÃO\033[m!")
else:
    print("Você está \033[1;31mREPROVADO\033[m.")