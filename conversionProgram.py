
from tkinter import *
def listToString(s):
    str1 = ""
    return(str1.join(s))
def decToBin():
    z = []
    x = int(lEntry.get())
    while True:
        t = x % 2
        z.append(str(t))
        x = x // 2
        if x == 0:
            break
    z.reverse()
    y = listToString(z)
    print(y)
    rEntry.delete(0,END)
    rEntry.insert(0,y)

def binToDec():
    x = rEntry.get()
    y = int(x,2)
    print(y)
    lEntry.delete(0,END)
    lEntry.insert(0,y)
    
print("1. Decimal To Binary")
print("2. Binary to Hexadecimal")
print("3. Hexadecimal to Decimal")
which = input("Enter: ")

if which == "1":
    main = Tk()
    main.title("Decimal To Binary")
    main.geometry("300x90")
    lLbl = Label(main,text="Decimal").grid(column=0,row=0,padx=4,pady=4)
    rLbl = Label(main,text="Binary").grid(column=1,row=0,padx=4,pady=4)
    lEntry = Entry(main)
    lEntry.grid(column=0,row=1,padx=4,pady=4)
    mLbl = Label(main,text="<->").grid(columnspan=2,row=1,padx=4,pady=4)
    rEntry = Entry(main)
    rEntry.grid(column=1,row=1,padx=4,pady=4)

    Button(main,text="Dec To Bin",command=decToBin).grid(column=0,row=2,padx=20,pady=4)
    Button(main,text="Bin to Dec",command=binToDec).grid(column=1,row=2,padx=20,pady=4)



    main.grid_columnconfigure(0,weight=1)
    main.grid_columnconfigure(1,weight=1)
    main.grid_rowconfigure(0,weight=1)

    # mainloop, runs infinitely
    mainloop()

