
distance = 0
energy = 10
eat = (energy + 2) 
spacer = "\n------------------------------------------------------------------------------ \n"

print("Your energy level is full at 10. \n Eat or walk to gain energy. \n")

while distance >= 0:  
    choice = input("\nPick a choice, type 'walk' or 'run' \n").lower()
    
    if choice == 'walk':
        distance += 1
        energy += 1
        print(spacer + "\tDistance from home is {}km\t Your energy level is : {}".format(distance, energy) + spacer)
    elif choice == 'run':
        distance += 5 
        energy -= 2
        print(spacer + "\tDistance from home is {}km\t Your energy level is : {}".format(distance, energy) + spacer)
        if energy <= 0: 
            print(spacer + "You have no energy, walk to cool off!")
            break # quits the program needs fix 
    elif choice == 'go home': 
        print(spacer + "\tDistance from home is {}km\t Your energy level is : {}".format(distance, energy) + spacer)
        break 
    elif choice == "eat": 
        energy += 2
        print(spacer + "\tDistance from home is {}km\t Your energy level is : {}".format(distance, energy) + spacer)
    else: 
        print("Something went wrong")
        print(spacer + "\tDistance from home is {}km\t Your energy level is : {}".format(distance, energy) + spacer)

