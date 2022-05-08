#---------------------#
# Char to Hexadecimal #
# Hexadecimal to Char #
#---------------------#
from tkinter import *
def listToString(s):
    str1 = ""
    return(str1.join(s))
def charToHex():
    k = []
    y = []
    z = lEntry1.get()
    x = list(z)
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
    print(k)
    k = listToString(k)
    rEntry1.delete(0,END)
    rEntry1.insert(0,k)

def hexToChar():
    t = []
    x = rEntry1.get()
    x = x.split(" ")
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
    t = listToString(t)
    print(t)
    lEntry1.delete(0,END)
    lEntry1.insert(0,t)
main = Tk()
main.title("Character To Hexadecimal")
main.geometry("300x90")
lLbl1 = Label(main,text="Character").grid(column=0,row=0,padx=4,pady=4)
rLbl1 = Label(main,text="Hexadecimal").grid(column=1,row=0,padx=4,pady=4)
lEntry1 = Entry(main)
lEntry1.grid(column=0,row=1,padx=4,pady=4)
mLbl1 = Label(main,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
rEntry1 = Entry(main)
rEntry1.grid(column=1,row=1,padx=4,pady=4)



Button(main,text="Char To Hex",command=charToHex).grid(column=0,row=2,padx=20,pady=4)
Button(main,text="Hex to Char",command=hexToChar).grid(column=1,row=2,padx=20,pady=4)



main.grid_columnconfigure(0,weight=1)
main.grid_columnconfigure(1,weight=1)
main.grid_rowconfigure(0,weight=1)

# mainloop, runs infinitely
mainloop()
