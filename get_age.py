age = input("Enter your age. \t")
older = int(age) - 24 
younger = 24 - int(age) 

if int(age) == 24: 
    print("\nWe are the same age! ")
elif int(age) == 23: 
    print('You are younger by 1 year')
elif int(age) == 25: 
    print('You are older by 1 year')
elif int(age) > 105: 
    print('I\'m not sure I believe you!') 
elif int(age) > 24 and int(age) < 105:
    print("\nYour older than me by {} years.".format(older))
elif int(age) < 24 and int(age) > 2: 
    print('You are younger by {} years'.format(younger))
else: 
    print("Something went wrong!")

