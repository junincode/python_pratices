from time import sleep
def Maior(*l):
    mai = 0
    for i, c in enumerate(l):
        if i == 1 or c > mai:
            mai = c
    print("=-"*20)
    print(f"{"ANÁLISE":^40}")
    print("=-"*20)
    for c in l:
        print(c, end=" ")
        sleep(0.2)
    print(f"Foram informados {len(l)} valores ao total.")
    print(f"O Maior dos valores é {mai}")
    sleep(1)


Maior(10, 9, 23, 45, 109, 110, 32)
Maior(3, 10, 9, 18, -5 )
Maior()
Maior(1, 3)
Maior(0, 1 , 1, 2, 3, 5, 8, 13)

