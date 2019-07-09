secret_number = 43

def guessed(): 
    user_guess = input("Guess my secret number!\n")
    guess = int(user_guess)

    if guess == secret_number: 
        print("You Win!")
    elif guess == 44 or guess == 42:
        print("So close!")
        guessed()
    else: 
        print("Try again!")
        guessed()
        
    
guessed()