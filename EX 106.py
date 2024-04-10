from time import sleep as sl
r = " "
def alin(msg):
    print("\033[1;41m~"*(len(msg)+4))
    print(f"  {msg}")
    print("~"*(len(msg)+4))
def Procurando(msg):
    print("\033[1;43m~" * (len(msg) + 4))
    print(f"  {msg}")
    print("~" * (len(msg) + 4))
while True:
    alin("SISTEMA DE AJUDA PyHELP")
    r = input("\033[mFunção ou Biblioteca>> \033[40m")
    if r.lower() == "fim":
        break
    Procurando(f"ACESSANDO O MANUAL DO COMANDO '{r}'")
    sl(1)
    print("\033[7;40m")
    help(f"{r.lower()}"), print("\033[m")

print("Fim do programa")

