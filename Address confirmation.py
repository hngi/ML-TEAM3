#importing libraries

import pandas as pd
import googlemaps

gmaps = googlemaps.Client(key='INSERT KEY HERE')

# input address
address= input("Enter address: ")

# Geocoding an address
geocode_result = gmaps.geocode(address)

if geocode_result == []:
    print ("This address is invalid")
else:
    geocode_result= geocode_result[0]
    
    if 'plus_code' in geocode_result:
        print("The Company address is valid")
    else:
        print("This address is vague, This job invite is likely a scam")

