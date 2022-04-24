import arbys, kfc
from arbys import get_arbys
from kfc import get_kfc

print("Search for these Restauraunt Selections in your town: \n\n - Arby's\n - KFC\n\nPlease type the full restaurant name as a selection\n\nYou can also type 'q' to quit\n")
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
    else:
        print('')
        print("ERROR: Please enter a valid input.")
        print('')
        restaurant_selection = input("Which restauraunt would you like to search for?: ").lower()