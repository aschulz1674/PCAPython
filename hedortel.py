from random import *
for i in range(3):
    x = randint(0,1)
    y = input("Guess which side: ")
    if y.strip().lower() == "tails":
        z = 0
    if y.strip().lower() == "heads":
        z = 1
    if z == x:
        print("You guessed",y,"and got it right!")
    
    else:
        print("Sorry its wrong, maybe try again?")