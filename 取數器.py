# coding=UTF-8
from tkinter import *
import tkinter
import os
path = os.path.dirname(os.path.abspath(__file__))
import random as rd
import pyperclip as pp

win = Tk() 
win.title("取數器") 
win.geometry("400x200+0+0") 
win.minsize(width="400", height="65") 
win.resizable(0, 1) 
win.iconbitmap(path+"/images/icon.ico") 
win.config(background="white") 
win.attributes("-alpha", 1) 

AllResults = ""

def copy_results():
    global AllResults
    pp.copy(AllResults)

def get_nb():
    global AllResults
    AllResults = ""
    try:
        enbg = int(enb.get())
        ensg = int(ens.get())
        enspg = int(ensp.get())
        entig = int(enti.get())
    except ValueError:
        win2 = Tk() 
        win2.title("取數器") 
        win2.geometry("400x120+400+0") 
        win2.minsize(width="400", height="65") 
        win2.resizable(0, 0) 
        win2.iconbitmap(path+"/images/icon.ico") 
        win2.config(background="white") 
        win2.attributes("-alpha", 1) 

        lb = Label(win2, text="-錯誤-", bg="red", fg="white", height=1, width=45)
        lb.place(anchor="nw", x=0, y=0)

        lb = Label(win2, text="「輸入欄」不得為空", height=1)
        lb.place(anchor="nw", x=0, y=30)
        lb = Label(win2, text="「輸入值」須為數值", height=1)
        lb.place(anchor="nw", x=0, y=60)
        lb = Label(win2, text="「輸入值」須為整數", height=1)
        lb.place(anchor="nw", x=0, y=90)
    if enbg - ensg + 1 <= 1:
        win2 = Tk() 
        win2.title("取數器") 
        win2.geometry("400x60+400+0") 
        win2.minsize(width="400", height="65") 
        win2.resizable(0, 0) 
        win2.iconbitmap(path+"/images/icon.ico") 
        win2.config(background="white") 
        win2.attributes("-alpha", 1) 

        lb = Label(win2, text="-錯誤-", bg="red", fg="white", height=1, width=45)
        lb.place(anchor="nw", x=0, y=0)

        lb = Label(win2, text="「可選取數數目」必須大於一", height=1)
        lb.place(anchor="nw", x=0, y=30)

    elif entig > (enbg - ensg + 1)/enspg:
        win2 = Tk() 
        win2.title("取數器") 
        win2.geometry("400x60+400+0") 
        win2.minsize(width="400", height="65") 
        win2.resizable(0, 0) 
        win2.iconbitmap(path+"/images/icon.ico") 
        win2.config(background="white") 
        win2.attributes("-alpha", 1) 

        lb = Label(win2, text="-錯誤-", bg="red", fg="white", height=1, width=45)
        lb.place(anchor="nw", x=0, y=0)

        lb = Label(win2, text="「取數數目」不可大於「可選取數數目」", height=1)
        lb.place(anchor="nw", x=0, y=30)

    else:
        win2 = Tk() 
        win2.title("取數器") 
        win2.geometry("400x" + str(30+entig*20) + "+400+0") 
        win2.minsize(width="400", height="65") 
        win2.resizable(0, 0) 
        win2.iconbitmap(path+"/images/icon.ico") 
        win2.config(background="white") 
        win2.attributes("-alpha", 1) 

        lb = Label(win2, text="-結果-", bg="yellow", fg="orange", height=1, width=45)
        lb.place(anchor="nw", x=0, y=0)

        btn = Button(win2, text="複製")
        btn.config(command=copy_results)
        btn.place(anchor="nw", x=340, y=30)

        MyList = []
        while entig > 0:
            MyResults = rd.randrange(ensg, enbg+1, enspg)
            tf = MyResults in MyList
            if tf == False:
                lb = Label(win2, text=MyResults, height=1)
                lb.place(anchor="nw", x=0, y=entig*20)
                entig = entig-1
                MyList.append(MyResults)
                AllResults = str(MyResults) + "\n" + str(AllResults)

def about_this():
    win3 = Tk() 
    win3.title("取數器") 
    win3.geometry("400x120+400+0") 
    win3.minsize(width="400", height="65") 
    win3.resizable(0, 0) 
    win3.iconbitmap(path+"/images/icon.ico") 
    win3.config(background="white") 
    win3.attributes("-alpha", 1) 

    lb = Label(win3, text="-關於-", bg="yellow", fg="orange", height=1, width=45)
    lb.place(anchor="nw", x=0, y=0)
    lb = Label(win3, text="1)本軟體由貓虎皮開發", height=1)
    lb.place(anchor="nw", x=0, y=30)
    lb = Label(win3, text="2)感謝您的下載，歡迎多加利用", height=1)
    lb.place(anchor="nw", x=0, y=60)
    lb = Label(win3, text="3)如有問題，請聯絡「5j.vm0.m3@gmail.com」", height=1)
    lb.place(anchor="nw", x=0, y=90)
            
lb = Label(win, text="-設置-", bg="yellow", fg="orange", height=1, width=45)
lb.place(anchor="nw", x=0, y=0)

lb = Label(win, text="最大數值", height=1)
lb.place(anchor="nw", x=0, y=30)

enb = Entry(win)
enb.place(anchor="nw", x=60, y=30, height=20)

lb = Label(win, text="最小數值", height=1)
lb.place(anchor="nw", x=0, y=60)

ens = Entry(win)
ens.place(anchor="nw", x=60, y=60, height=20)

lb = Label(win, text="取數間隔", height=1)
lb.place(anchor="nw", x=0, y=90)

ensp = Entry(win)
ensp.place(anchor="nw", x=60, y=90, height=20)

lb = Label(win, text="取數數目", height=1)
lb.place(anchor="nw", x=0, y=120)

enti = Entry(win)
enti.place(anchor="nw", x=60, y=120, height=20)

btn = Button(win, text="執行")
btn.config(command=get_nb)
btn.place(anchor="nw", x=5, y=150)

btn = Button(win, text="關於")
btn.config(command=about_this)
btn.place(anchor="nw", x=60, y=150)

win.mainloop()