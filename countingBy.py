#User enters a number to count by
while True:
    try:
        #User enters a number
        x = int(input("Enter a number to count by: "))
        #Above 0 and it moves on
        if x > 0:
            break
        #Not above 0 and it tries the input again
        else:
            print("Error, enter a positive number.")
            continue
    #If the user enters something thats not an integer it tries the input again
    except ValueError:
        print("Error, enter a number.")
        continue
# User enters a number to count to
while True:
    try:
        #User enters a number
        y = int(input("Enter a number to count to: "))
        #If above 0 continues
        if y > 0:
           #If the counting to number is divisible by the counting number continue 
           if y % x < 1:
               break
           #If not try input again
           else:
                print("Error, enter a number divisible by your counting number.") 
                continue
        #If 0 or below try again
        else:
            print("Error, enter a positive number.")
            continue
    #Trys again if not an integer
    except ValueError:
        print("Error, enter a number.")
        continue
#Starts at 0, ends at user number inputed + counting number(So it doesnt end short), and counts by counting number
for i in range(0,y + x,x):
    #Prints numbers being counted
    print(i)