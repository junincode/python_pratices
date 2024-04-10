class Escola():
    def __init__(self, quantidade):
        self.pessoas = quantidade


p = int(input("Quantas pessoas havia na igreja? "))
a = Escola()
print(f"Na igreja havia {a.pessoas}")
