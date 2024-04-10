r = " "
mm20 = 0
mi, qh, c = 0, 0, 0
while r not in "Nn":
    c += 1
    print("{}° CADASTRO".format(c))
    n = input("Nome do usuário: ")
    s = input("SEXO [M/F]: ")
    while s not in "FfMm":
        s = input("RESPOSTA INVÁLIDA. SEXO [M/F]: ")
    i = int(input("Idade: "))
    if i < 18:
        mi += 1
    if s in "Mm":
        qh += 1
    if i < 20 and s in "Ff":
        mm20 += 1
    r = input("DESEJA CADASTRAR MAIS ALGUÉM? [S/N] ")
    while r not in "SsNn":
        r = input("RESPOSTA INVÁLIDA. DESEJA CADASTRAR MAIS ALGUÉM? [S/N]  ")
    print("="*20)
print('''Total de pessoas cadastradas: {}
Menores de idade: {}
Homens cadastrados: {}
Mulheres menores de 20 anos: {}'''.format(c, mi, qh, mm20))