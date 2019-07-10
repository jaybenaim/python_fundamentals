secret_number = 44

def guessed(): 
    user_guess = input("Guess my secret number!\n")
    guess = int(user_guess)

    if guess == secret_number: 
        print("You Win!")
    elif guess == 43 or guess == 45:
        print("So close!")
        guessed()
    else: 
        print("Try again!")
        guessed()
        
    
guessed()



