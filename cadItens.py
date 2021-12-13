from tkinter import *
from tkinter import ttk
from datetime import date
import banco
import os
import pyautogui

def insertEntry():
    v_item = str(tb_code1.get())
    v_quant = tb_quantity1.get()

    if tb_code1.get() and tb_quantity1.get() != "":

        vquery = "INSERT INTO tb_itens (T_DATA, T_ITEM, N_QUANTIDADE) VALUES('"+f_today+"','"+v_item +"','"+str(v_quant)+"')"
        banco.dml(vquery)
        tb_code1.delete(0, END)
        tb_quantity1.delete(0, END)

        print('O item:', v_item, ', foi cadastrado com:', v_quant, 'unidade(s)')
        print('-' * 90)
    else:
        pyautogui.alert(title= 'ERRO', text='Não foi possível dar saída! Todos os campos são obrigatórios')

pastaApp=os.path.dirname(__file__)

app = Tk()

today = date.today()
f_today = today.strftime("%d/%m/%Y")

black = "#000"
green = "#008100"
white =  "#ffffff"

app.iconbitmap(default='./assets/icons.ico')
app.title("CADASTRO DE ITENS")
app.state("zoomed")
app.configure(bg="#ffffff")

imgLogo=PhotoImage(file=pastaApp+"\\./assets/logo.png")
nb=ttk.Notebook(app)
nb.place(x=0,y=0,relwidth=1,relheight=1)

# 1
nb1=Frame(nb)
nb.add(nb1,text="Entrada")

lb_logo1 = Label(nb1,image=imgLogo).pack(fill=X)

lb_title1 = Label(nb1,text="Cadastre seu item", fg=green, font="Verdana 17").pack(fill=X, pady=80)

lb_code1=Label(nb1,text="Código do Item", fg=green, font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_code1 = Entry(nb1)
tb_code1.pack(fill=X, pady=10, padx=200, anchor="w")

lb_quantity1=Label(nb1,text="Quantidade", fg=green, font="Verdana 12", anchor="w").pack(fill=X, pady=10, padx=200, anchor="w")
tb_quantity1 = Entry(nb1)
tb_quantity1.pack(fill=X, pady=10, padx=200, anchor="w")

tb_data1 = Label(nb1, text=f_today, font="Verdana 8", fg=green).place(x=0,y=0)

Button(nb1, text="Cadastrar", bg=green, fg=white, border=2, font="Verdana 12", command=insertEntry).pack(fill=X, pady=30, padx=700, anchor="w")

app.mainloop()
input()
