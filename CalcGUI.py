import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=210
        height=294
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_12=tk.Button(root)
        GButton_12["activebackground"] = "#ededed"
        GButton_12["activeforeground"] = "#000000"
        GButton_12["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "1"
        GButton_12["relief"] = "flat"
        GButton_12.place(x=10,y=90,width=40,height=40)
        GButton_12["command"] = self.GButton_12_command

        GButton_392=tk.Button(root)
        GButton_392["activebackground"] = "#ededed"
        GButton_392["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_392["font"] = ft
        GButton_392["fg"] = "#000000"
        GButton_392["justify"] = "center"
        GButton_392["text"] = "2"
        GButton_392["relief"] = "flat"
        GButton_392.place(x=60,y=90,width=40,height=40)
        GButton_392["command"] = self.GButton_392_command

        GButton_412=tk.Button(root)
        GButton_412["activebackground"] = "#ededed"
        GButton_412["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_412["font"] = ft
        GButton_412["fg"] = "#000000"
        GButton_412["justify"] = "center"
        GButton_412["text"] = "6"
        GButton_412["relief"] = "flat"
        GButton_412.place(x=110,y=140,width=40,height=40)
        GButton_412["command"] = self.GButton_412_command

        GButton_999=tk.Button(root)
        GButton_999["activebackground"] = "#ededed"
        GButton_999["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_999["font"] = ft
        GButton_999["fg"] = "#000000"
        GButton_999["justify"] = "center"
        GButton_999["text"] = "4"
        GButton_999["relief"] = "flat"
        GButton_999.place(x=10,y=140,width=40,height=40)
        GButton_999["command"] = self.GButton_999_command

        GButton_473=tk.Button(root)
        GButton_473["activebackground"] = "#ededed"
        GButton_473["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_473["font"] = ft
        GButton_473["fg"] = "#000000"
        GButton_473["justify"] = "center"
        GButton_473["text"] = "8"
        GButton_473["relief"] = "flat"
        GButton_473.place(x=60,y=190,width=40,height=40)
        GButton_473["command"] = self.GButton_473_command

        GButton_113=tk.Button(root)
        GButton_113["activebackground"] = "#ededed"
        GButton_113["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_113["font"] = ft
        GButton_113["fg"] = "#000000"
        GButton_113["justify"] = "center"
        GButton_113["text"] = "9"
        GButton_113["relief"] = "flat"
        GButton_113.place(x=110,y=190,width=40,height=40)
        GButton_113["command"] = self.GButton_113_command

        GButton_381=tk.Button(root)
        GButton_381["activebackground"] = "#ededed"
        GButton_381["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_381["font"] = ft
        GButton_381["fg"] = "#000000"
        GButton_381["justify"] = "center"
        GButton_381["text"] = "5"
        GButton_381["relief"] = "flat"
        GButton_381.place(x=60,y=140,width=40,height=40)
        GButton_381["command"] = self.GButton_381_command

        GButton_101=tk.Button(root)
        GButton_101["activebackground"] = "#ededed"
        GButton_101["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_101["font"] = ft
        GButton_101["fg"] = "#000000"
        GButton_101["justify"] = "center"
        GButton_101["text"] = "3"
        GButton_101["relief"] = "flat"
        GButton_101.place(x=110,y=90,width=40,height=40)
        GButton_101["command"] = self.GButton_101_command

        GButton_96=tk.Button(root)
        GButton_96["activebackground"] = "#ededed"
        GButton_96["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_96["font"] = ft
        GButton_96["fg"] = "#000000"
        GButton_96["justify"] = "center"
        GButton_96["text"] = "0"
        GButton_96["relief"] = "flat"
        GButton_96.place(x=60,y=240,width=40,height=40)
        GButton_96["command"] = self.GButton_96_command

        GButton_461=tk.Button(root)
        GButton_461["activebackground"] = "#ededed"
        GButton_461["bg"] = "#ffffff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_461["font"] = ft
        GButton_461["fg"] = "#000000"
        GButton_461["justify"] = "center"
        GButton_461["text"] = "7"
        GButton_461["relief"] = "flat"
        GButton_461.place(x=10,y=190,width=40,height=40)
        GButton_461["command"] = self.GButton_461_command

        GButton_10=tk.Button(root)
        GButton_10["activebackground"] = "#d6d6d6"
        GButton_10["bg"] = "#e8e8e8"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_10["font"] = ft
        GButton_10["fg"] = "#000000"
        GButton_10["justify"] = "center"
        GButton_10["text"] = "."
        GButton_10["relief"] = "flat"
        GButton_10.place(x=110,y=240,width=40,height=40)
        GButton_10["command"] = self.GButton_10_command

        GButton_241=tk.Button(root)
        GButton_241["activebackground"] = "#f4f3ec"
        GButton_241["bg"] = "#fffef7"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_241["font"] = ft
        GButton_241["fg"] = "#000000"
        GButton_241["justify"] = "center"
        GButton_241["text"] = "+"
        GButton_241["relief"] = "flat"
        GButton_241.place(x=160,y=90,width=40,height=40)
        GButton_241["command"] = self.GButton_241_command

        GButton_836=tk.Button(root)
        GButton_836["activebackground"] = "#f4f3ec"
        GButton_836["bg"] = "#fffef7"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_836["font"] = ft
        GButton_836["fg"] = "#000000"
        GButton_836["justify"] = "center"
        GButton_836["text"] = "-"
        GButton_836["relief"] = "flat"
        GButton_836.place(x=160,y=140,width=40,height=40)
        GButton_836["command"] = self.GButton_836_command

        GButton_447=tk.Button(root)
        GButton_447["activebackground"] = "#f4f3ec"
        GButton_447["bg"] = "#fffef7"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_447["font"] = ft
        GButton_447["fg"] = "#000000"
        GButton_447["justify"] = "center"
        GButton_447["text"] = "x"
        GButton_447["relief"] = "flat"
        GButton_447.place(x=160,y=240,width=40,height=40)
        GButton_447["command"] = self.GButton_447_command

        GButton_358=tk.Button(root)
        GButton_358["activebackground"] = "#b7d2ea"
        GButton_358["bg"] = "#b4dcff"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_358["font"] = ft
        GButton_358["fg"] = "#000000"
        GButton_358["justify"] = "center"
        GButton_358["text"] = "="
        GButton_358["relief"] = "flat"
        GButton_358.place(x=10,y=240,width=40,height=40)
        GButton_358["command"] = self.GButton_358_command

        GMessage_934=tk.Message(root)
        GMessage_934["anchor"] = "nw"
        GMessage_934["bg"] = "#ffffff"
        GMessage_934["cursor"] = "arrow"
        ft = tkFont.Font(family='Arial',size=10)
        GMessage_934["font"] = ft
        GMessage_934["fg"] = "#000000"
        GMessage_934["justify"] = "center"
        GMessage_934["text"] = x
        GMessage_934["relief"] = "flat"
        GMessage_934.place(x=10,y=10,width=190,height=60)

        GButton_470=tk.Button(root)
        GButton_470["activebackground"] = "#f4f3ec"
        GButton_470["bg"] = "#fffef7"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_470["font"] = ft
        GButton_470["fg"] = "#000000"
        GButton_470["justify"] = "center"
        GButton_470["text"] = "÷"
        GButton_470["relief"] = "flat"
        GButton_470.place(x=160,y=190,width=40,height=40)
        GButton_470["command"] = self.GButton_470_command

    def GButton_12_command(self):
        print("command")


    def GButton_392_command(self):
        print("command")


    def GButton_412_command(self):
        print("command")


    def GButton_999_command(self):
        print("command")


    def GButton_473_command(self):
        print("command")


    def GButton_113_command(self):
        print("command")


    def GButton_381_command(self):
        print("command")


    def GButton_101_command(self):
        print("command")


    def GButton_96_command(self):
        print("command")


    def GButton_461_command(self):
        print("command")


    def GButton_10_command(self):
        print("command")


    def GButton_241_command(self):
        print("command")


    def GButton_836_command(self):
        print("command")


    def GButton_447_command(self):
        print("command")


    def GButton_358_command(self):
        print("command")


    def GButton_470_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
