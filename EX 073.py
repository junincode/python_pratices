t = ('Palmeiras',
'Botafogo',
'Flamengo',
'Grêmio',
'Bragantino',
'Atlético - MG',
'Athletico - PR',
'Fluminense',
'Cuiabá',
'São Paulo',
'Fortaleza',
'Corinthians',
'Internacional',
'Santos',
'Vasco',
'Cruzeiro',
'Bahia',
'Goiás',
"Coritiba",
"América - MG")

print(t[:5])
print(t[16:])
print('''G5--------------''')
for c in range(0, 5):
    print(f"{c+1}° - {t[c]} ")
print("Z4------------------")
for c in range(16, 20):
    print(f"{c+1}° - {t[c]}")
print(f"Em ordem alfabética: {sorted(t)}")
print(F"O FLAMENGO ESTÁ NA POSIÇÃO: {t.index("Flamengo")+1}°")
