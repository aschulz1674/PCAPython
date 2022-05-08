from tkinter import *
import math
def listToString(s):
    str1 = ""
    return(str1.join(s))
def decToBin():
    z = []
    x = lEntry2.get()
    x = int(x)
    while True:
        t = x % 2
        z.append(str(t))
        x = x // 2
        if x == 0:
            break
    z.reverse()
    y = listToString(z)
    L1L.set("Dec To Bin: " + y)

def binToDec():
    x = rEntry2.get()
    y = int(x,2) 
    y = str(y)
    R1L.set("Bin To Dec: " + y)
root = Tk()
root.title("Decimal To Binary")
root.geometry("300x90")
lLbl2 = Label(root,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
rLbl2 = Label(root,text="Binary").grid(column=1,row=0,padx=4,pady=4)
L1L = StringVar(root)
L1L.set("Dec To Bin: ")
L2L = Label(root,textvariable=L1L)
L2L.grid(column=0,row=2,padx=20,pady=4)
R1L = StringVar(root)

R1L.set("Bin To Dec: ")
R2L = Label(root,textvariable=R1L)
R2L.grid(column=1,row=2,padx=20,pady=4)
lEntry2 = Entry(root)
lEntry2.grid(column=0,row=1,padx=4,pady=4)
mLbl2 = Label(root,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
rEntry2 = Entry(root)
rEntry2.grid(column=1,row=1,padx=4,pady=4)

Button(root,text="Dec To Bin",command=decToBin).grid(column=0,row=3,padx=20,pady=4)
rrr =Button(root,text="Bin to Dec",command=binToDec).grid(column=1,row=3,padx=20,pady=4)


root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
mainloop()
