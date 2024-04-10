Listagem = ("COMPUTADOR", 4500,
            "LAPIS", 1.5,
            "ABAJUR", 30,
            "BLUSA", 59.9,
            "ESTOJO", 19.9,
            "CARREGAGOR", 19.9,
            "MOUSEPAD", 59.9,
            "FONE DE OUVIDO", 99.9,
            "CANECA", 9.9)
print("="*35)
print(f"{"LISTAGEM DE PREÇOS":^35}")
print("="*35)
for i in range(0, len(Listagem), 2):
    print(f"{Listagem[i]:.<28}R${Listagem[i+1]:.2f}")