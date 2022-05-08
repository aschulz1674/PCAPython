from tkinter import *
from random import *


theNumbah = randrange(1,11)
tries = 3
restarb = False
def restart():
    global tries
    global theNumbah
    global restarb
    buttonLbl.set("Go again?")
    theNumbah = randrange(1,11)
    restarb = True

def show_answer():
    global theNumbah
    global tries
    global restarb
    if restarb == True:
        restarb = False
        lbl.set("Guess a number from 1-10")
        buttonLbl.set("Show")
        num1.delete(0,END)
        tries = 3
        triStr = str(tries)
        labl.set("Tries: "+ triStr)
        return()
    triStr = str(tries)
    labl.set("Tries: " + triStr)
    number = num1.get()
    number = int(number)
    if tries > 0:
        if number == theNumbah:
            lbl.set("You Guessed It!!")
            restart()
        elif number > theNumbah:
            lbl.set("Too high.")
            tries -= 1
            triStr = str(tries)
            labl.set("Tries: "+ triStr )
        elif number < theNumbah:
            lbl.set("Too low.")
            tries -= 1
            triStr = str(tries)
            labl.set("Tries: "+ triStr )
    if tries <= 0:
        lbl.set("Goodluck next time.")
        restart()
    labl.set("Tries: "+ triStr )
    
        
    


main = Tk()

main.title("Guessing Game")
main.geometry("265x125")
main.resizable(False,False)
lbl = StringVar()
lbl.set("Guess a number from 1-10")
bruh = Label(main, textvariable=lbl).grid(row=0,columnspan=2)
numLbl = Label(main,text="Enter A Number:",padx=2)
numLbl.grid(row=1,column=0,sticky=E+W,padx=4,pady=4)
num1 = Entry(main)
num1.grid(row=1,column=1,sticky=W,padx=4,pady=4)

labl = StringVar()
triStr = str(tries)
labl.set("Tries: "+ triStr )
Label(main,textvariable=labl).grid(row=2,columnspan=2)



buttonLbl = StringVar()
buttonLbl.set("Show")
Button(main,text='Quit',command=main.destroy).grid(row=3,column=0,sticky=N+S,pady=4,padx=4)
Button(main,textvariable=buttonLbl,command=show_answer).grid(row=3,column=1,sticky=N+S,pady=4,padx=4)
main.grid_columnconfigure(1,weight=1)
main.grid_columnconfigure(0,weight=1)
main.grid_rowconfigure(0,weight=1)
main.grid_rowconfigure(1,weight=1)
main.grid_rowconfigure(2,weight=1)
main.grid_rowconfigure(4,weight=1)
mainloop()