
distance = 0

while distance >= 0:  
    choice = input("Pick a choice, type 'walk' or 'run' \n").lower()
    
    if choice == 'walk':
        distance += 1
        print("Distance from home is {}km".format(distance))
    elif choice == 'run':
        distance += 5 
        print("Distance from home is {}km".format(distance))
    elif choice == 'go home': 
        print("Distance to home is {}km".format(distance))
        break 
    else: 
        print("Something went wrong")
        print("Distance to home is {}km".format(distance))




