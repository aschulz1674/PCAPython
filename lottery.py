from random import *
x = list(str(randint(100,999)))
y = list(str(input("Guess the loterry numbers: ")))
z = 0
for i in y:
    if i in x:
        z += 1
if z == 1:
    print(str(x))
    print(str(y))
    print("1000$!")
elif z == 2:
    print(str(x))
    print(str(y))
    print("3000$!")
elif z == 3:
    print(str(x))
    print(str(y))
    print("10000$!")
else:
    print("LOSER!")

