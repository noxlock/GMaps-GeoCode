'''
Program that uses Google's API to perform Geocode operations
Author: Hunter Kemp
Email:  CSS011905@coderacademy.edu.au
'''

import googlemaps


GMAPS = googlemaps.Client(key="AIzaSyA4uZQUmMn3gP-5L759AyG0v9j8-gM89vc")

#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

'''
for dict_item in geocode_result:
for key in dict_item:
count += 1

print(geocode_result[0]['formatted_address'])



location format = street # street name, city state
'''


def is_valid_latlong(latitude, longitude):
    '''
    checks whether input for location() is valid
    INPUT: latitude, longitude
    OUTPUT: True or prints error and sends to gmaps_menu()
    '''

    try:
        if latitude.isdigit() is True and longitude.isdigit() is True:
            latitude, longitude = int(latitude), int(longitude)
            # tests ifdigit to prep for int cast

        if latitude > 90 or longitude > 180:
            print("""Error! Invalid values, Latitude = 0-90,
            Longitude = 0-180""")
            # makes sure you can't do stupid big numbers
        if latitude < -90 or longitude < -180:
            print("""Error! Invalid values, Latitude = 0-90,
            Longitude = 0-180""")
            #makes sure you can't do stupid tiny numbers
        else:
            return True
            #returns True for the actual function
    except:
        print("Error: Invalid Values!")
        gmaps_menu()
        # catch for initial isdigit()

def location(latitude, longitude):
    '''
    converts latitude and longitude to location
    INPUT: latitude, longitude
    OUTPUT: location, or error if nothing at coordinates
    '''
    count = 0

    if is_valid_latlong(latitude, longitude) is True: 
        # if test returns True, continue with function
        reverse_geocode_result = GMAPS.reverse_geocode((latitude, longitude))
        # uses Google API to search coordinates, sets it to a variable

        for dict_item in reverse_geocode_result:
            for key in dict_item:
                count = count + 1
                #iterates the list and dictionary

        if not reverse_geocode_result:
            print("Sorry, we couldn't find anything there!")
        else:
            print(reverse_geocode_result[0]['formatted_address'])
            # if list empty, print error, else print address




def is_valid_location(streetnumberstreetname, citystate):
    pass

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
                count = count + 1
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
        latitude = input("Please enter a latitude 0-90\n")
        longitude = input("Please enter a longitude 0-180\n")
        location(latitude, longitude)
    elif choice == "random":
        randomloc()
    elif choice == "exit":
        quit()

gmaps_menu()
