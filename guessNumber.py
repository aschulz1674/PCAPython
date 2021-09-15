from random import * 
while True:
    rating = 0
    print("Guess a number between 0 and 50")
    print("--------------------------------")
    number = randrange(0,51)
    while number != rating:
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


