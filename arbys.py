# IF YOUR TOWN DOES NOT HAVE AN ARBY'S
# -- It will redirect to your state locations
# -- Otherwise it will redirect to the main locations page (all states)

# external modules
import geocoder
import webbrowser

from geopy.geocoders import *
from geocoder import location, ipinfo

# own modules
import states
from states import states_abr

def get_arbys():

    your_location = (geocoder.ip("me"))
    your_lat_long = your_location.latlng
    your_state = str(your_location).split()[5][0:-1]
    your_state_abbr = ""
    your_town = str(your_location).split()[4][1:-1]
    condensed_town = ""

    # checking for towns with spaces

    for letter in your_town.split():
        condensed_town += letter

    # getting your states abbreviation
    for i in states_abr:
        if states_abr.get(i) == your_state:
            your_state_abbr = i.lower()
            break

    arbys_in_town = (f'https://locations.arbys.com/{your_state_abbr.lower()}/{condensed_town.lower()}/')

    # If you have Google Chrome, replace 'chrome_path' with your file path. (Make sure to include the %s at the end.)

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open_new_tab(arbys_in_town)
