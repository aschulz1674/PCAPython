from tkinter import *
import math
from typing import Counter
def mainDestroy():
    kain.withdraw()
def listToString(s):
    str1 = ""
    return(str1.join(s))
###################################################################
def main():
    kain.withdraw()
    def rip():
        kain.deiconify()
        main.destroy()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry1.get()
                if x == "":
                    rEntry1.delete(0,END)
                    return
                x = int(x)
                while True:
                    t = x % 2
                    z.append(str(t))
                    x = x // 2
                    if x == 0:
                        break
                z.reverse()
                y = listToString(z)
                rEntry1.delete(0,END)
                rEntry1.insert(-1,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry1.get()
                if x == "":
                    lEntry1.delete(0,END)
                    return
                y = int(x,2)
                lEntry1.delete(0,END)
                lEntry1.insert(0,y)
                break
            except:
                break
    def check():
        x = str(main.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        main.after(50,check)
    def listToString(s):
        str1 = ""
        return(str1.join(s))
    main = Tk()
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    main.title("Decimal To Binary")
    main.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    
    lLbl1 = Label(main,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl1 = Label(main,text="Binary").grid(column=1,row=0,padx=4,pady=4)
    lEntry1 = Entry(main)
    lEntry1.grid(column=0,row=1,padx=4,pady=4)
    mLbl1 = Label(main,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry1 = Entry(main,justify='right')
    rEntry1.grid(column=1,row=1,padx=4,pady=4)
    check()
    main.grid_columnconfigure(0,weight=1)
    main.grid_columnconfigure(1,weight=1)
    main.grid_rowconfigure(0,weight=1)
    main.protocol("WM_DELETE_WINDOW",rip)
    mainloop()  
###################################################################
def root():
    kain.withdraw()
    def rip():
        kain.deiconify()
        root.withdraw()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry2.get()
                if x == "":
                    rEntry2.delete(0,END)
                    return
                ###########
                y = str(hex(int(x)))
                ###########
                rEntry2.delete(0,END)
                rEntry2.insert(0,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry2.get()
                if x == "":
                    lEntry2.delete(0,END)
                    return
                ###########
                n = int(x,16) 
                bStr = ''
                while n > 0:
                    bStr = str(n % 2) + bStr
                    n = n >> 1    
                z = bStr
                y = int(z,2)
                ##########
                lEntry2.delete(0,END)
                lEntry2.insert(0,y)
                break
            except:
                break
    def check():
        x = str(root.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        root.after(50,check)
    root = Tk()
    root.title("Decimal To Hexadecimal")
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    root.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    lLbl2 = Label(root,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl2 = Label(root,text="Hexadecimal").grid(column=1,row=0,padx=4,pady=4)
    lEntry2 = Entry(root)
    lEntry2.grid(column=0,row=1,padx=4,pady=4)
    mLbl2 = Label(root,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry2 = Entry(root)
    rEntry2.grid(column=1,row=1,padx=4,pady=4)
    check()
    
    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=1)
    root.grid_rowconfigure(0,weight=1)
    # rootloop, runs infinitely
    root.protocol("WM_DELETE_WINDOW",rip)
    mainloop()
###################################################################
def bruh():
    kain.withdraw()
    def rip():
        kain.deiconify()
        bruh.withdraw()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry3.get()
                if x == "":
                    rEntry3.delete(0,END)
                    return
                ###########
                n = int(x,16) 
                bStr = ''
                while n > 0:
                    bStr = str(n % 2) + bStr
                    n = n >> 1    
                y = bStr
                ###########
                rEntry3.delete(0,END)
                rEntry3.insert(0,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry3.get()
                if x == "":
                    lEntry3.delete(0,END)
                    return
                ###########
                
                z = int(x,2)
                y = str(hex(int(z)))
                ##########
                lEntry3.delete(0,END)
                lEntry3.insert(0,y)
                break
            except:
                break
    def check():
        x = str(bruh.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        bruh.after(50,check)
    bruh = Tk()
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    bruh.title("Hexadecimal To Binary")
    bruh.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    lLbl3 = Label(bruh,text="Hexadecimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl3 = Label(bruh,text="Binary").grid(column=1,row=0,padx=4,pady=4)
    lEntry3 = Entry(bruh)
    lEntry3.grid(column=0,row=1,padx=4,pady=4)
    mLbl3 = Label(bruh,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry3 = Entry(bruh)
    rEntry3.grid(column=1,row=1,padx=4,pady=4)
    check()
    bruh.grid_columnconfigure(0,weight=1)
    bruh.grid_columnconfigure(1,weight=1)
    bruh.grid_rowconfigure(0,weight=1)
    # bruhloop, runs infinitely
    bruh.protocol("WM_DELETE_WINDOW",rip)
    mainloop()
###################################################################
def duh():
    kain.withdraw()
    def rip():
        kain.deiconify()
        duh.withdraw()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry4.get()
                if x == "":
                    rEntry4.delete(0,END)
                    return
                ###########
                y = []
                x = x.split(" ")
                if x[-1] == "":
                    x.pop(-1)
                for i in range(len(x)):
                    if x[i] != " ":
                        x[i] = int(x[i])
                        x[i] = chr(x[i])
                
                y = listToString(x)
                ###########
                rEntry4.delete(0,END)
                rEntry4.insert(0,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry4.get()
                if x == "":
                    lEntry4.delete(0,END)
                    return
                ###########
                z = []
                y = list(x)
                for i in range(len(y)):
                    z.append(str(ord(y[i])))
                    z.append(" ")
                z.pop(-1)
                y = listToString(z)
                
                ##########
                lEntry4.delete(0,END)
                lEntry4.insert(0,y)
                break
            except:
                break
    def check():
        x = str(duh.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        duh.after(50,check)
    duh = Tk()
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    duh.title("Decimal To Character")
    duh.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    lLbl4 = Label(duh,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl4 = Label(duh,text="Character").grid(column=1,row=0,padx=4,pady=4)
    lEntry4 = Entry(duh)
    lEntry4.grid(column=0,row=1,padx=4,pady=4)
    mLbl4 = Label(duh,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry4 = Entry(duh)
    rEntry4.grid(column=1,row=1,padx=4,pady=4)
    check()
    duh.grid_columnconfigure(0,weight=1)
    duh.grid_columnconfigure(1,weight=1)
    duh.grid_rowconfigure(0,weight=1)
    # duhloop, runs infinitely
    duh.protocol("WM_DELETE_WINDOW",rip)
    mainloop()
###################################################################
def cuh():
    kain.withdraw()
    def rip():
        kain.deiconify()
        cuh.withdraw()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry5.get()
                if x == "":
                    rEntry5.delete(0,END)
                    return
                ###########
                t = []
                x = x.split(" ")
                if x[-1] == "":
                    x.pop(-1)
                for i in range(len(x)):
                    if x[i] != "":
                        t.append(x[i])
                x = t
                t = []
                for i in range(len(x)):
                    y = int(x[i],2)
                    y = chr(y)
                    t.append(y)
                y = listToString(t)
                ###########
                rEntry5.delete(0,END)
                rEntry5.insert(0,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry5.get()
                if x == "":
                    lEntry5.delete(0,END)
                    return
                ###########
                k = []
                y = []
                x = list(x)
                for i in range(len(x)):
                    x[i] = int(ord(x[i]))
                for i in range(len(x)):
                    y = []
                    j = x[i]
                    while True:
                        y.append(str(j%2))
                        j = j // 2
                        if j == 0:
                            break
                    y.reverse()
                    y = listToString(y)
                    k.append(y)
                    k.append(" ")
                y = listToString(k)
                ##########
                lEntry5.delete(0,END)
                lEntry5.insert(0,y)
                break
            except:
                break
    def check():
        x = str(cuh.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        cuh.after(50,check)
    cuh = Tk()
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    cuh.title("Binary To Character")
    cuh.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    lLbl5 = Label(cuh,text="Binary").grid(column=0,row=0,padx=4,pady=4)
    rLbl5 = Label(cuh,text="Character").grid(column=1,row=0,padx=4,pady=4)
    lEntry5 = Entry(cuh)
    lEntry5.grid(column=0,row=1,padx=4,pady=4)
    mLbl5 = Label(cuh,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry5 = Entry(cuh)
    rEntry5.grid(column=1,row=1,padx=4,pady=4)
    check()
    cuh.grid_columnconfigure(0,weight=1)
    cuh.grid_columnconfigure(1,weight=1)
    cuh.grid_rowconfigure(0,weight=1)
    # cuhloop, runs infinitely
    cuh.protocol("WM_DELETE_WINDOW",rip)
    mainloop()
###################################################################
def suh():
    kain.withdraw()
    def rip():
        kain.deiconify()
        suh.withdraw()
    def convert1():
        z = []
        while True:
            try:
                x = lEntry6.get()
                if x == "":
                    rEntry6.delete(0,END)
                    return
                ###########
                t = []
                x = x.split(" ")
                if x[-1] == "":
                    x.pop(-1)
                for i in range(len(x)):
                    n = int(x[i],16) 
                    bStr = ''
                    while n > 0:
                        bStr = str(n % 2) + bStr
                        n = n >> 1    
                    z = bStr
                    y = int(z,2)
                    t.append(y)
                    
                for i in range(len(t)):
                    t[i] = chr(t[i])
                y = listToString(t)
                ###########
                rEntry6.delete(0,END)
                rEntry6.insert(0,y)
                break
            except:
                break
    def convert2():
        while True:
            try:
                x = rEntry6.get()
                if x == "":
                    lEntry6.delete(0,END)
                    return
                ###########
                k = []
                y = []
                x = list(x)
                for i in range(len(x)):
                    x[i] = int(ord(x[i]))
                for i in range(len(x)):
                    y = []
                    j = x[i]
                    while True:
                        y.append(str(j%2))
                        j = j // 2
                        if j == 0:
                            break
                    y.reverse()
                    y = listToString(y)
                    k.append(y)
                    k.append(" ")
                for i in range(len(k)):
                    if k[i] != " ":
                        z = int(k[i],2)
                        k[i] = str(hex(int(z)))
                y = listToString(k)
                ##########
                lEntry6.delete(0,END)
                lEntry6.insert(0,y)
                break
            except:
                break
    def check():
        x = str(suh.focus_get())
        
        if x == ".!entry2":
            convert2()
        elif x == ".!entry":
            convert1()
        suh.after(50,check)
    suh = Tk()
    lv_x = kain.winfo_rootx()
    lv_y = kain.winfo_rooty()
    suh.title("Hexadecimal To Character")
    suh.geometry('%dx%d+%d+%d' % (300, 50, lv_x, lv_y))
    lLbl6 = Label(suh,text="Hexadecimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl6 = Label(suh,text="Character").grid(column=1,row=0,padx=4,pady=4)
    lEntry6 = Entry(suh)
    lEntry6.grid(column=0,row=1,padx=4,pady=4)
    mLbl6 = Label(suh,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry6 = Entry(suh)
    rEntry6.grid(column=1,row=1,padx=4,pady=4)
    check()
    suh.grid_columnconfigure(0,weight=1)
    suh.grid_columnconfigure(1,weight=1)
    suh.grid_rowconfigure(0,weight=1)
    # suhloop, runs infinitely
    suh.protocol("WM_DELETE_WINDOW",rip)
    mainloop()
###################################################################
kain = Tk()
def switch1():
    b1.configure(text="Bin To Dec",command=main)
    b2.configure(text="Dec To Hex",command=root)
    b3.configure(text="Hex to Bin",command=bruh)
    b4.configure(text="Character Conversions",command=switch2)
def switch2():
    b1.configure(text="Bin To Char",command=cuh)
    b2.configure(text="Dec To Char",command=duh)
    b3.configure(text="Hex to Char",command=suh)
    b4.configure(text="Numerical Conversions",command=switch1)
kain.title("Conversion Programs")
kain.geometry("300x100")
b1 = Button(kain,text="Bin To Dec",command=main,width=10)
b2 = Button(kain,text="Dec To Hex",command=root,width=10)
b3 = Button(kain,text="Hex To Bin",command=duh,width=10)
b4 = Button(kain,text="Character Conversions",command=switch2,width=50)
b1.grid(column=0,row=0,padx=15,pady=4)
b2.grid(column=1,row=0,padx=15,pady=4)
b3.grid(column=2,row=0,padx=15,pady=4)
b4.grid(columnspan=3,row=1,padx=15,pady=5)

kain.grid_columnconfigure(0,weight=1)
kain.grid_columnconfigure(1,weight=1)
kain.grid_columnconfigure(2,weight=1)
kain.grid_rowconfigure(0,weight=1)
kain.grid_rowconfigure(1,weight=1)
mainloop()