nl1, nl2 = [], []


class Solution:
    def addTwoNumbers(self, l1, l2):
        nova_soma = []
        l1.reverse()
        l2.reverse()

        nl1 = map(str, l1)
        nl2 = map(str, l2)


        texto_1 = str("".join(nl1))
        texto_2 = str("".join(nl2))
        soma = eval(f"{texto_1} + {texto_2}")

        return(int(soma))

a = Solution()
print(a.addTwoNumbers([8, 3, 2, 5],[4, 4, 9]))