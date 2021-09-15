from turtle import * 
speed(0)
pendown()

# Code for conch shell 
def square(side):
    for i in range(4):
        forward(side)
        left(90)
def squareCircle():
    sLength = 3
    
    x = 1

    for i in range(122):
        if x == 1:
            color("black")
            x = x + 1
        else:
            color("pink")
            x = x / 2
        square(sLength)
        left(3)
        sLength = sLength + 3
# Code for the equilateral triangle
def equilTri(size):
    pensize(5)
    x = ["red","blue","green"]
    f = 0
    for i in range(3):
        color(x[f])
        forward(size)
        left(120)
        f = f + 1
# Code for the 5 pointed star
def star(size):
   
    left(72)
    for i in range(5):
        forward(size)
        right(144)
    
# Code for the star spiral 
def starSpiral():
    x = 5
    r = ["darkgray","gray","silver","gold","gray","silver"]
    f = 0
    for i in range(7):
        for y in r:
            print(f)
            color(r[f])
            star(x)
            left(15)
            x *= 1.15
            f += 1
        f = 0
            

#squareCircle()
 
#equilTri(120)
 
#star(100)
   
starSpiral()


input()
