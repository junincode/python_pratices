import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for i in range(tamanho))
    return password

if __name__ == "__main__":
    length = int(input("Qual o comprimento da senha? "))
    password = gerar_senha(length)
    print(f"A senha gerada é: {password}")


