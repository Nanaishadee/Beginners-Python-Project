#code for the user to guess
import random

def guess(x):
    random_number= random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Ooops, guess again. Too low")
        elif guess < random_number:
            print("Got ya, better luck next time. Too high")

    print(f"Someone got luck today!! You have  the number {random_number} right ")
    
    # code for the computer to guess
def program_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c": 
        if low != high:
             guess = random.randint(low, high) 
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? .lower() ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        
    print(f"Bravo! The program guessed your number, {guess} correctly!" )
program_guess(1000)
