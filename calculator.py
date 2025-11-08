from tkinter import *
import re
root = Tk()
root.geometry("600x600")
def clear():
    l1.config(text="")
    
def ans():
    ans = l1.cget('text')
    l1.config(text=ans)
    
def disp(i):
    l1.config(text=str(l1.cget('text'))+str(i.cget('text')))
    
def ans():
    ans = l1.cget('text')
    #print(list(l1.cget('text')))
    if('+' in ans):
        tup = ans.split("+")
        tot = float(tup[0]) + float(tup[1])
        l1.config(text=tot)
    elif('-' in ans):
        print(ans.split("-"))
        tup = ans.split("-")
        tot = float(tup[0]) - float(tup[1])
        l1.config(text=tot)
    elif('*' in ans):
        tup = ans.split("*")
        tot = float(tup[0]) * float(tup[1])
        l1.config(text=tot)
    elif('/' in ans):
        tup = ans.split("/")
        tot = float(tup[0]) / float(tup[1]) 
        l1.config(text=tot)

l1 = Label(root,text="",relief=SUNKEN,height=5,width=50,bg="white")
l1.grid(row=0,column=0,columnspan = 5)      
 

b0 = Button(text=0,width=10,height=5,padx=0,command=lambda: disp(b0))
b0.grid(row=1,column=1)
b1 = Button(text=1,width=10,height=5,padx=0,command=lambda: disp(b1))
b1.grid(row=1,column=2)
b2 = Button(text=2,width=10,height=5,padx=0,command=lambda: disp(b2))
b2.grid(row=1,column=3)

b3 = Button(text=3,width=10,height=5,padx=0,command=lambda: disp(b3))
b3.grid(row=2,column=1)
b4 = Button(text=4,width=10,height=5,padx=0,command=lambda: disp(b4))
b4.grid(row=2,column=2)
b5 = Button(text=5,width=10,height=5,padx=0,command=lambda: disp(b5))
b5.grid(row=2,column=3)

b6 = Button(text=6,width=10,height=5,padx=0,command=lambda: disp(b6))
b6.grid(row=3,column=1)
b7 = Button(text=7,width=10,height=5,padx=0,command=lambda: disp(b7))
b7.grid(row=3,column=2)
b8 = Button(text=8,width=10,height=5,padx=0,command=lambda: disp(b8))
b8.grid(row=3,column=3)
b9 = Button(text=9,width=10,height=5,padx=0,command=lambda: disp(b9))
b9.grid(row=4,column=1)

clear = Button(text="C",width=10,height=5,padx=0,command=clear)
clear.grid(row=4,column=2)

minus = Button(text="-",width=10,height=5,padx=0,command=lambda: disp(minus))
minus.grid(row=2,column=4)

multi = Button(text="*",width=10,height=5,padx=0,command=lambda: disp(multi))
multi.grid(row=3,column=4)

divide = Button(text="/",width=10,height=5,padx=0,command=lambda: disp(divide))
divide.grid(row=4,column=4)

eq = Button(text="=",width=10,height=5,padx=0,command=ans)
eq.grid(row=4,column=3)

plus = Button(text="+",width=10,height=5,padx=0,command=lambda: disp(plus))
plus.grid(row=1,column=4)
