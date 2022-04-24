# IF YOUR TOWN DOES NOT HAVE A KFC
# -- It will redirect to the normal location search page (all states)

# external modules
import socket
import geocoder
import webbrowser

from geopy.geocoders import *
from geocoder import location, ipinfo
from socket import gethostname, getaddrinfo

# own modules
import states
from states import states_abr

# web scraping arbys

your_device = socket.gethostname()
your_device_info = socket.getaddrinfo(your_device, 3000)
your_ip = your_device_info[2][4][0]
your_location = (geocoder.ip("me"))
your_lat_long = your_location.latlng
your_state = str(your_location).split()[5][0:-1]
your_state_abbr = ""
your_town = str(your_location).split()[4][1:-1]
condensed_town = ""

condensed_town = your_town.replace(' ', '-')

for i in states_abr:
    if states_abr.get(i) == your_state:
        your_state_abbr = i.lower()
        break

kfc_in_town = f'https://locations.kfc.com/{your_state_abbr.lower()}/{condensed_town.lower()}'

webbrowser.open_new_tab(kfc_in_town)