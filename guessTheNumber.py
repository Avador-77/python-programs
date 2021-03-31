import random

def guess(x):
    random_number = random.randint(1, x)

    guess = int(input(f"Guess a number between 1 to {x}:"))
    while guess != random_number:
        if guess < random_number:
            print("nope, that's not correct. Too low.")
            guess = int(input(f"Guess a number between 1 to {x} again:"))
        
        else:
            print("nope, that's not correct. Too high.")
            guess = int(input(f"Guess a number between 1 to {x} again:"))

    print(f"yeah, congratualtions. You guessed the number {guess} right")


guess(10)
        
