import arbys, kfc, pizzahut, tacobell
from arbys import get_arbys
from kfc import get_kfc
from pizzahut import get_pizzahut
from tacobell import get_tacobell

print("Search for these Restauraunt Selections in your town: \n\n - Arby's\n - KFC\n - Pizza Hut \n - Taco Bell \n\nPlease type the full restaurant name as a selection\n\nYou can also type 'q' to quit\n")
restaurant_selection = input("Which restauraunt would you like to search for?: ").lower()
while restaurant_selection != 'q':
    if restaurant_selection == "Arby's".lower():
        get_arbys()
        print('')
        print('Please restart the program to search again.')
        break
    elif restaurant_selection == 'KFC'.lower():
        get_kfc()
        print('')
        print("Please restart the program to search again.")
        break
    elif restaurant_selection == "Pizza Hut".lower():
        get_pizzahut()
        print('')
        print("Please restart the program to search again.")
        break
    elif restaurant_selection == "Taco Bell".lower():
        get_tacobell()
        print('')
        print("Please restart the program to search again.")
        break
    else:
        print('')
        print("ERROR: Please enter a valid input.")
        print('')
        restaurant_selection = input("Which restauraunt would you like to search for?: ").lower()