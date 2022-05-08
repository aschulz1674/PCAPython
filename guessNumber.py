from random import * 
while True:
    rating = -5
    while True:
        try:
            x = int(input("What range of numbers do you want?: "))
            break
        except ValueError:
            print("Error, enter a number.")
            continue
    while True:
        try:
            eg = int(input("How many tries do you want?: "))
            break
        except ValueError:
            print("Error, enter a number.")
            continue
    print("Guess a number between 0 and", x)
    print("--------------------------------")
    number = randrange(0,x + 1)
    tries = 0
    while number != rating and tries < eg:
        while True:
            try:
                rating = int(input("Guess the secret number: "))
                break
            except ValueError:
                print("Error enter a number.")
        if rating > number:
            print("Too high.")
        elif rating < number:
            print("Too low.")
        tries += 1
    if tries >= eg:
        print("You failed.")
    else:
        print("You guessed it!")
    while True:
        x = input("Go again? (y/n): ").strip().lower()
        if x == "y" or x == "n":
            break
        else:
            print("Error enter a valid input.")
            continue
    if x == "y":
        continue
    if x == "n":
        print("Goodbye.")
        break


