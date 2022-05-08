from tkinter import *
import math
def listToString(s):
    str1 = ""
    return(str1.join(s))
def decToHex():
    x = lEntry2.get()
    y = str(hex(int(x)))
    L1L.set("Dec To Hex: " + y)
def hexToDec():
    x = rEntry2.get()
    n = int(x,16) 
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1    
    z = bStr
    y = int(z,2)
    y = str(y)
    R1L.set("Hex To Dec: " + y)
root = Tk()
root.title("Decimal To Hexadecimal")
root.geometry("300x90")
lLbl2 = Label(root,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
rLbl2 = Label(root,text="Hexadecimal").grid(column=1,row=0,padx=4,pady=4)
L1L = StringVar(root)
L1L.set("Dec To Hex: ")
L2L = Label(root,textvariable=L1L)
L2L.grid(column=0,row=2,padx=20,pady=4)
R1L = StringVar(root)

R1L.set("Hex To Dec: ")
R2L = Label(root,textvariable=R1L)
R2L.grid(column=1,row=2,padx=20,pady=4)
lEntry2 = Entry(root)
lEntry2.grid(column=0,row=1,padx=4,pady=4)
mLbl2 = Label(root,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
rEntry2 = Entry(root)
rEntry2.grid(column=1,row=1,padx=4,pady=4)

Button(root,text="Dec To Hex",command=decToHex).grid(column=0,row=3,padx=20,pady=4)
rrr =Button(root,text="Hex to Dec",command=hexToDec).grid(column=1,row=3,padx=20,pady=4)


root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
mainloop()
