'''
Program that uses Google's API to perform Geocode operations
Author: Hunter Kemp
Email:  CSS011905@coderacademy.edu.au
'''

import googlemaps
from random import randint


GMAPS = googlemaps.Client(key="AIzaSyA4uZQUmMn3gP-5L759AyG0v9j8-gM89vc")

#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')





def is_greater(lat, longitude):
    '''
    checks if lat, long are greater than 
    or less than their max, min values
    INPUT: lat, longitude
    OUTPUT: return True OR print error
    '''

    if lat > 90 or lat < -90:
        print("Error: Latitude ranges from -90 - 90")
    elif longitude > 180 or longitude < -180:
        print("Error: Longitude ranges from -180 - 180")
    else:
        return True




def is_int(lat, longitude):
    '''
    tries to cast lat, longitude to int
    INPUT: lat, longitude
    OUTPUT: int(lat), int(longitude) OR return False
    '''

    try:
        lat = int(lat)
        longitude = int(longitude)
        return True
    except ValueError:
        return False





def is_float(lat, longitude):
    '''
    tries to cast lat, longitude to float
    INPUT: lat, longitude
    OUTPUT: float(lat), float(longitude) OR return False
    '''

    try:
        lat = float(lat)
        longitude = float(longitude)
        return True
    except ValueError:
        return False





def location(lat, longitude):
    '''
    does final check, with is_greater
    INPUT: latitude, longitude
    OUTPUT if numbers valid, calls reverse_geo_search
    '''


    if is_int(lat, longitude) is True:
        lat = int(lat)
        longitude = int(longitude)
        if is_greater(lat, longitude) is True:
            reverse_geo_search(lat, longitude)
        #tries to cast to int, else tries to cast to float

    elif is_float(lat, longitude) is True:
        lat = float(lat)
        longitude = float(longitude)
        if is_greater(lat, longitude) is True:
            reverse_geo_search(lat, longitude)

    else:
        print("Error: Invalid values!")
        #if neither work, print error



def reverse_geo_search(lat, longitude):
    count = 0

    reverse_geocode_result = GMAPS.reverse_geocode((lat, longitude))
    # uses Google API to search coordinates, sets it to a variable

    for dict_item in reverse_geocode_result:
        for key in dict_item:
            count += 1
            #iterates the list and dictionary
            if not reverse_geocode_result:
                print("Sorry, we couldn't find anything there!")
            else:
                print(reverse_geocode_result[0]['formatted_address'])
                quit()
                # if list empty, print error, else print address 






def latlong():
    count = 0
    print("Please enter your street number followed by your street name, e.g: ")
    streetnumberstreetname = input("118 Walker Street\n")
    #asks for street number & name

    print("Please entre your city followed by your state, e.g: ")
    citystate = input("North Sydney NSW\n")
    #asks for city and state

    geocode_result = GMAPS.geocode(streetnumberstreetname + citystate)

    for dict_item in geocode_result:
            for key in dict_item:
                count += 1
                # iterates list and dictionary

            print(geocode_result[0]['geometry']['location'])







def gmaps_menu():
    '''
    Prints the menu for GeoCode.py
    '''

    print("- - - - - - - - -\nWhat would you like to do?")
    print("[latlong] Converts a location to lat/longitude")
    print("[location] Converts lat/longitude to location.")
    print("[random] Generates a random location\n[Exit] Stops the program")
    choice = input("- - - - - - - - -\n")

    if choice == "latlong":
        latlong()
    elif choice == "location":
        lat = input("Please enter a latitude 0-90\n")
        longitude = input("Please enter a longitude 0-180\n")
        location(lat, longitude)
    elif choice == "random":
        randomloc()
    elif choice == "exit":
        quit()

gmaps_menu()
