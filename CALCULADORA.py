from tkinter import *

all_values = ""
def entrar_valores(event):
    global all_values
    all_values = all_values + str(event)

    valor_texto.set(all_values)

def calcular(event):
    global all_values
    global resultado
    resultado = eval(event)
    valor_texto.set(resultado)
    all_values = str(resultado)


def limpar_tela():
    global all_values
    all_values = ""
    valor_texto.set(all_values)


# INTERFACE DA CALCULADORA

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
frame_tela = Frame(janela, width=235, height=50, bg= "#000000")
frame_tela.grid(row=0, column=0)
frame_resto = Frame(janela, width=235, height=268, bg= "#3b3b3b")
frame_resto.grid()

#LABEL

valor_texto = StringVar()
clc_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, bg="#000000",
fg="#ffffff", padx=7, relief=FLAT, anchor="e", justify= LEFT, font="Ivy 13 bold")
clc_label.place(x=60, y=0)


# BOTÕES

b_1 = Button(frame_resto, command= lambda: limpar_tela(), text="C", width=16, height=2, bg="#e0e0e0", relief=RAISED, overrelief=RIDGE) #CLEAN
b_1.place(x=0, y=0)
b_2 = Button(frame_resto, command= lambda: entrar_valores("%"),text="%", width=5, height=2, bg="#e0e0e0") #PORCENTAGEM
b_2.place(x=134, y=0)
b_3 = Button(frame_resto, command= lambda: entrar_valores("/"),text="/", width=5, height=2, bg="#e68c05", fg="#ffffff") #DIVISÃO
b_3.place(x=188, y=0)
b_4 = Button(frame_resto, command= lambda: entrar_valores("7"),text="7", width=7, height=2, bg="#e0e0e0") # 7
b_4.place(x=0, y=49)
b_5 = Button(frame_resto, command= lambda: entrar_valores("8"),text="8", width=7, height=2, bg="#e0e0e0") # 8
b_5.place(x=62.5, y=49)
b_6 = Button(frame_resto, command= lambda: entrar_valores("9"),text="9", width=7, height=2, bg="#e0e0e0") # 9
b_6.place(x=126, y=49)
b_7 = Button(frame_resto, command= lambda: entrar_valores("*"),text="*", width=5, height=2, bg="#e68c05", fg="#ffffff") # *
b_7.place(x=188, y=49)
b_8 = Button(frame_resto, command= lambda: entrar_valores("4"),text="4", width=7, height=2, bg="#e0e0e0") # 4
b_8.place(x=0, y=98)
b_8 = Button(frame_resto, command= lambda: entrar_valores("5"),text="5", width=7, height=2, bg="#e0e0e0") # 5
b_8.place(x=62.5, y=98)
b_9 = Button(frame_resto, command= lambda: entrar_valores("6"),text="6", width=7, height=2, bg="#e0e0e0") # 6
b_9.place(x=126, y=98)
b_10 = Button(frame_resto, command= lambda: entrar_valores("-"),text="-", width=5, height=2, bg="#e68c05", fg="#ffffff") # -
b_10.place(x=188, y=98)
b_10 = Button(frame_resto, command= lambda: entrar_valores("+"),text="+", width=5, height=2, bg="#e68c05", fg="#ffffff") # +
b_10.place(x=188, y=147)
b_11 = Button(frame_resto, command= lambda: entrar_valores("3"),text="3", width=7, height=2, bg="#e0e0e0") # 3
b_11.place(x=126, y=147)
b_12 = Button(frame_resto, command= lambda: entrar_valores("2"),text="2", width=7, height=2, bg="#e0e0e0") # 2
b_12.place(x=62.5, y=147)
b_13 = Button(frame_resto, command= lambda: entrar_valores("1"),text="1", width=7, height=2, bg="#e0e0e0") # 1
b_13.place(x=0, y=147)
b_13 = Button(frame_resto, command= lambda: calcular(all_values),text="=", width=5, height=2, bg="#e68c05", fg="#ffffff") # =
b_13.place(x=188, y=196)
b_14 = Button(frame_resto, command= lambda: entrar_valores("."),text=",", width=7, height=2, bg="#e0e0e0") # ,
b_14.place(x=126, y=196)
b_15 = Button(frame_resto, command= lambda: entrar_valores("0"),text="0", width=15, height=2, bg="#e0e0e0") # 0
b_15.place(x=0, y=196)

#EXPRESSÕES

janela.mainloop()