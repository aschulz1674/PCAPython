from turtle import *
from typing import *
speed(0)
penup()
def PCA():
    setposition(-200,0)
    color("blue")
    for i in range(12):
        write("P",font=("Arial",32,"normal"))
        right(30)
        forward(10)
    backward(50)
    right(90)
    for i in range(15):
        write("P",font=("Arial",32,"normal"))
        forward(10)
    left(90)
    forward(150)
    left(180)
    color("gray")
    for i in range(36):
        write("C",font=("Arial",32,"normal"))
        right(5)
        forward(6.5)
    right(90)
    forward(150)
    left(90)
    forward(30)
    left(75)
    color("lightblue")
    for i in range(17):
        write("A",font=("Arial",32,"normal"))
        forward(10)
    right(140 )
    for i in range(18):
        write("A",font=("Arial",32,"normal"))
        forward(10)
    right(180)
    forward(90)
    left(75)
    for i in range(7):
        write("A",font=("Arial",32,"normal"))
        forward(7.5)
def software():
    color("black")
    write("WARE",font=("Comic Sans MS",64,"normal"))
    right(90)
    forward(75)
    left(90)
    forward(75)
    write("soft",font=("Impact",64,"normal"))
def hela():
    color("orange")
    pendown()
    pensize(5)
    right(90)
    forward(100)
    right(60)
    forward(75)
    right(120)
    forward(100)
    right(60)
    forward(75)
    right(60)
    forward(75)
    right(60)
    forward(100)
    right(120)
    forward(75)
    penup()
    forward(25)
    left(30)
    forward(32)
    color("black")
    write("HE",font=("Comic Sans MS",28,"normal"))
    right(180)
    forward(60)
    write("LA",font=("Comic Sans MS",28,"normal"))
def pick():
    while True:
        print("Pick which logo: ")
        print("PCA,Software,HELA")
        x = input("Pick: ").strip().lower()
        if x == "pca":
            PCA()
            break
        elif x == "software":
            software()
            break
        elif x == "hela":
            hela()
            break
        else:
            print("Enter a correct input.")
            continue
while True:
    pick()
    while True:
        h = input("Go again?(y/n): ").strip().lower()
        if h == "y" or h == "n":
            break
        else:
            print("Enter a correct input.")
            continue
    if h == "y":
        clear()
        continue
    elif h == "n":
        break
    else:
        print("Bruh what did you do how did you break this your not supposed to see this.")
        continue

    

input()