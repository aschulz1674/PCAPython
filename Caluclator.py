while True: 
    x = input("Enter a operator(+ , - , * , /) : ")
    while True:
        if x == "*":
            o = "multiply"
            break
        elif x == "/":
            o = "divide"
            break
        elif x == "+":
            o = "add"
            break
        elif x == "-":
            o = "subtract"
            break
        else:
            x = input("Error, enter a valid input: ")
            continue
    tex = "Enter a number to " + o + ": "
    while True:
        try:
            y = float(input(tex))
            break
        except ValueError:
            print("Error enter a number.")
            continue
    while True:
        try:
            z = float(input(tex))
            break
        except ValueError:
            print("Error enter a number.")
            continue
    if x == "*":
        e = y * z
        e = round(e,4)
        print(str(y) + " x " + str(z) + " = " + str(e))
    elif x == "/":
        e = y / z
        e = round(e,4)
        print(str(y) + " ÷ " + str(z) + " = " + str(e))
    elif x == "+":
        e = y + z
        e = round(e,4)
        print(str(y) + " + " + str(z) + " = " + str(e))
    elif x == "-":
        e = y - z  
        e = round(e,4)                                        
        print(str(y) + " - " + str(z) + " = " + str(e))
    while True:
        ans = input("Go again? (y/n): ")
        if ans == "y" or ans == "n":
            break
        else:
            print("Invalid Input.")
            continue
    if ans == "y":
        continue
    elif ans == "n":
        print("Goodbye.")
        break