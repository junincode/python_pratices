s = 0
m1000, c, pmb = 0, 0, 0
mb, r = " ", " "
while r not in "Nn":
    c += 1
    n = input("Nome do produto: ")
    p = float(input("Preço: R$"))
    if c == 1:
        mb = n
        pmb = p
    if p < pmb:
        pmb = p
        mb = n
    s += p
    if p > 1000:
        m1000 += 1
    r = input("Qual comprar mais alguma coisa? [S/N]? ").strip()
    while r not in "SsNn":
        r = input("RESPOSTA INVÁLIDA. Qual comprar mais alguma coisa? [S/N]? ")
    print("="*20)
print('''TOTAL DE PRODUTOS: {}
NOME DO PRODUTO MAIS BARATO: {} CUSTANDO R${}
PRODUTOS DE MAIS DE R$1000: {}
TOTAL GASTO NA COMPRA: R${:.2f}'''.format(c, mb, pmb, m1000, s))