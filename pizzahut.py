# IF YOUR TOWN DOES NOT HAVE A PIZZA HUT
# -- It will redirect to the normal location search page (all states)

# external modules
import geocoder
import webbrowser

from geopy.geocoders import *
from geocoder import location, ipinfo

# own modules
import states
from states import states_abr

def get_pizzahut():

    your_location = (geocoder.ip("me"))
    your_lat_long = your_location.latlng
    your_state = str(your_location).split()[5][0:-1]
    your_state_abbr = ""
    your_town = str(your_location).split()[4][1:-1]
    condensed_town = ""

    if len(your_state) != 2:
        your_state = str(your_location).split()[6][0:-1]
        your_town = (str(your_location).split()[4] + ' ' + str(your_location).split()[5])[1:-1]

    condensed_town = your_town.replace(' ', '-')

    for i in states_abr:
        if states_abr.get(i) == your_state:
            your_state_abbr = i.lower()
            break

    pizzahut_in_town = f'https://locations.pizzahut.com/{your_state_abbr.lower()}/{condensed_town.lower()}'

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" 

    # If you have Google Chrome, replace 'chrome_path' with your file path. (Make sure to include the %s at the end.)

    webbrowser.get(chrome_path).open_new_tab(pizzahut_in_town)