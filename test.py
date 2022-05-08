
from tkinter import *


class MyFirstGUI:
    def __init__(self, main):
        self.main = main
        main.title("A simple GUI")

        self.label = Label(main, text="- 2")
        self.labell = Label(main, text="+ 2")
        self.label.grid(column=1,row=0,padx=10,pady=4,sticky=EW)
        self.labell.grid(column=0,row=0,padx=10,pady=4,sticky=EW)
        self.e1 = Entry(main)
        self.e2 = Entry(main)
        self.e1.grid(column=0,row=1,padx=10,pady=4,sticky=W)
        self.e2.grid(column=1,row=1,padx=10,pady=4,stick=E)
        self.check()
    def convert2(self):
        while True:
            try:
                x = self.e2.get()
                if x == "":
                    self.e1.delete(0,END)
                    return
                x = int(x)
                y = x - 2
                self.e1.delete(0,END)
                self.e1.insert(0,y)
                break
            except:
                break
    def convert1(self):
        while True:
            try:
                x = self.e1.get()
                if x == "":
                    self.e2.delete(0,END)
                    return
                x = int(x)
                y = x + 2
                self.e2.delete(0,END)
                self.e2.insert(0,y)
                break
            except:
                break

        

        

    def check(self):
        x = str(root.focus_get())
        if x == ".!entry2":
            self.convert2()
        elif x == ".!entry":
            self.convert1()
        root.after(5,self.check)


root = Tk()
my_gui = MyFirstGUI(root)

root.mainloop()
