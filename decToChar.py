#----------------------#
# Decimal to Character #
# Character to Decimal #
#----------------------#
from tkinter import *
def listToString(s):
    str1 = ""
    return(str1.join(s))
def decToChar():
    y = []
    x = lEntry1.get()
    x = x.split(" ")
    for i in range(len(x)):
        if x[i] != " ":
            x[i] = int(x[i])
            x[i] = chr(x[i])
    y = listToString(x)
    print(y)
    rEntry1.delete(0,END)
    rEntry1.insert(0,y)

def charToDec():
    z = []
    x = rEntry1.get()
    y = list(x)
    for i in range(len(y)):
        z.append(str(ord(y[i])))
        z.append(" ")
    z = listToString(z)
    print(z)
    lEntry1.delete(0,END)
    lEntry1.insert(0,z)
main = Tk()
main.title("Decimal To Character")
main.geometry("300x90")
lLbl1 = Label(main,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
rLbl1 = Label(main,text="Character").grid(column=1,row=0,padx=4,pady=4)
lEntry1 = Entry(main)
lEntry1.grid(column=0,row=1,padx=4,pady=4)
mLbl1 = Label(main,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
rEntry1 = Entry(main)
rEntry1.grid(column=1,row=1,padx=4,pady=4)



Button(main,text="Dec To Char",command=decToChar).grid(column=0,row=2,padx=20,pady=4)
Button(main,text="Char to Dec",command=charToDec).grid(column=1,row=2,padx=20,pady=4)



main.grid_columnconfigure(0,weight=1)
main.grid_columnconfigure(1,weight=1)
main.grid_rowconfigure(0,weight=1)

# mainloop, runs infinitely
mainloop()
