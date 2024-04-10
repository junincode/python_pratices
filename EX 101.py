import datetime as dt
def VerifyVote(n):
    global a
    a = n
    if dt.datetime.today().year - n < 18:
        return "VOTO NEGADO"
    elif 18 <= dt.datetime.today().year - n < 21 or (dt.datetime.today().year - n) > 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"


a = int(input("ANO DE NASCIMENTO: "))
print(f"STATUS ===> Com {dt.datetime.today().year - a} anos >> {VerifyVote(a)}")