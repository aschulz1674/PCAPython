#----------------#
# Char to Binary #
# Binary to Char #
#----------------#
from tkinter import *
def listToString(s):
    str1 = ""
    return(str1.join(s))
def charToBin():
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
    k = listToString(k)
    print(k)
    rEntry1.delete(0,END)
    rEntry1.insert(0,k)

def binToChar():
    t = []
    z = rEntry1.get()
    x = z.split(" ")
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
    lEntry1.delete(0,END)
    lEntry1.insert(0,y)
main = Tk()
main.title("Char To Binary")
main.geometry("300x90")
lLbl1 = Label(main,text="Char").grid(column=0,row=0,padx=4,pady=4)
rLbl1 = Label(main,text="Binary").grid(column=1,row=0,padx=4,pady=4)
lEntry1 = Entry(main)
lEntry1.grid(column=0,row=1,padx=4,pady=4)
mLbl1 = Label(main,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
rEntry1 = Entry(main)
rEntry1.grid(column=1,row=1,padx=4,pady=4)



Button(main,text="Char To Bin",command=charToBin).grid(column=0,row=2,padx=20,pady=4)
Button(main,text="Bin to Char",command=binToChar).grid(column=1,row=2,padx=20,pady=4)



main.grid_columnconfigure(0,weight=1)
main.grid_columnconfigure(1,weight=1)
main.grid_rowconfigure(0,weight=1)

# mainloop, runs infinitely
mainloop()
