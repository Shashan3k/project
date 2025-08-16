import random

def guess_game(number, chances=8):
    if chances == 0:
        print(f"Out of chances! The number was {number}.")
        return
    
    try:
        guess = int(input(f"Guess a number (1-100), {chances} chances left: "))
    except ValueError:
        print("Not a valid number! Try again.")
        guess_game(number, chances)  
        return

    if guess == number:
        print("🎉 You got it! Well played.")
    elif guess < number:
        print("Too low!")
        guess_game(number, chances - 1)
    else:
        print("Too high!")
        guess_game(number, chances - 1)


number = random.randint(1, 100)
guess_game(number)
