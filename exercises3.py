# print("what is your name?")

# def print_hello(): 
#     ask = input("What is your name?\n").upper()
#     ask
#     a = "Hi "

# def variables(): 
#     age = 25
#     var = "My age is {}".format(24)
#     new_age = "Data is {}".format(type(age))
#     print(var)
#     print(new_age)
    

# # print_hello()
# # variables() 

# def new_user(): 
#     user_name = input() 
#     print("Hello, {}".format(user_name))

# new_user()

# def secret_pass(): 
#     secret_password = "jay"

#     print("What's the password?")
#     password_attempt = input()

#     correct_or_not = (password_attempt == secret_password)

#     print("That's {}!".format(correct_or_not))
# secret_pass()

# def cookies(): 
#     print("How many cookies have been eaten?")
#     eaten = input()
#     # convert user input to integer and subtract it from 12
#     remaining_cookies = 12 - int(eaten)
#     print("There are {} cookies left.".format(remaining_cookies))
# cookies() 

# def what_year(): 
#     age = input("What is your age? \n")
#     year = 2018 - int(age)  
#     print("You were born in {}".format(year))
# what_year()

# my_number = 5

# if my_number < 4:
#   print("Hello")
# print("Bonjour")

# if my_number > 4:
#   print("Hi there")
# print("How are you?")

# your_number = input()

# if int(your_number) > 5: 
#     print('This line will run if the user enters a number greater than 5')

# print("This line always runs") 

# number = input("Enter a number\n") 

# if int(number) > 0: 
#     print("{} is positive".format(number))
#     print(number + " is positive")
# else: 
#     print("{} is negative".format(number)) 
#     print(number + " is negative")

x = input("Enter an x-coordinate")
y = input("Enter an y-coordinate")

if int(x) > int(y): 
    print("x is greater than y!")
elif x < y: 
    print("x is less than y!")
else: 
    print("x is equal to y!")
    
