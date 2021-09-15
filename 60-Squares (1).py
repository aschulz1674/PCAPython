from turtle import * 
speed(0)
pendown()
def square(side):
    for i in range(4):
        forward(side)
        left(90)

def squareCircle():
    sLength = 3
    lColors = ["pink","black"]
    for i in range(80):
        
        square(sLength)
        left(5)
        sLength = sLength + 5
squareCircle()
