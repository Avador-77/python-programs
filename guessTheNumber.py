import random

def guess(x):
    random_number = random.randrange(x)
    chance  = 0
    guess = int(input(f"Guess a number between 1 to {x}:"))


    while guess != random_number:
        chance += 1
        if chance != 5:
            if guess < random_number:

                if chance == 4:
                    print("nope, that's not correct. Too low.")
                    guess = int(input(f"----This is the last chance----Guess a number between 1 to {x} again:"))
                else:
                    print("nope, that's not correct. Too low.")
                    guess = int(input(f"Guess a number between 1 to {x} again:"))
                
            else:

                if chance == 4:
                    print("nope, that's not correct. Too high.")
                    guess = int(input(f"----This is the last chance----Guess a number between 1 to {x} again:"))
                else:
                    print("nope, that's not correct. Too high.")
                    guess = int(input(f"Guess a number between 1 to {x} again:"))
        
        else:
            print("You Lost!!")
            break
    if guess == random_number:
        print(f"yeah, congratualtions. You guessed it, the number was {guess} ")

rangee = int(input("Enter the range in which you want to guess: "))
guess(rangee)
        
