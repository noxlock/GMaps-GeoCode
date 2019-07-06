#!/usr/bin/python3

'''
Program that uses Google's API to perform Geocode operations
Author: noxlock
'''

import random
import argparse
import googlemaps


GMAPS = googlemaps.Client(key="AIzaSyBt6Ma6ubAJ1jkY3JjPFXFJLkBhdStXyQw")




def is_greater(lat, longitude):
    '''
    checks if lat, long are greater than
    or less than their max, min values
    INPUT: lat, longitude
    OUTPUT: return True OR print error
    '''

    if lat > 90 or lat < -90:
        print("Error: Latitude ranges from -90 - 90")
        #checks lat isn't crazy high or low

    elif longitude > 180 or longitude < -180:
        #checks longitude isn't crazy high or low
        print("Error: Longitude ranges from -180 - 180")

    return True
    # if checks pass then return true




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
    # just tries to cast values to int




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
    # just tries to cast values to float





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
            return reverse_geo_search(lat, longitude)
        #tries to cast to int,

        #else tries to cast to float
    elif is_float(lat, longitude) is True:
        lat = float(lat)
        longitude = float(longitude)
        if is_greater(lat, longitude) is True:
            return reverse_geo_search(lat, longitude)


    return None





def reverse_geo_search(lat, longitude):
    '''
    converts lat/longitude to formatted address
    INPUT: lat, longitude
    OUTPUT: returns formatted addresss, or None
    '''

    reverse_geocode_result = GMAPS.reverse_geocode((lat, longitude))
    if reverse_geocode_result:
        return reverse_geocode_result[0]['formatted_address']
    return None
    # sets search results to variable, returns it





def latlong(streetnumberstreetname, citystate):
    '''
    converts formatted address to lat/longitude
    INPUT: streetnumberstreetname, citystate
    OUTPUT: lat, longitude
    '''


    geocode_result = GMAPS.geocode(streetnumberstreetname + citystate)

    if geocode_result:
        return geocode_result[0]['geometry']['location']
    return None
    #sets search results to variable, returns it



def randomloc(region):
    '''
    generates a random location within a region
    ARGUMENTS: "AUS", "NZ", "N"
    INPUT: None
    OUTPUT: formatted address
    '''

    if region == "AUS":
        randomlat = random.randint(-42, -12)
        randomlong = random.randint(113, 151)
        return reverse_geo_search(randomlat, randomlong)


    elif region == "NZ":
        randomlat = random.randint(-46, -34)
        randomlong = random.randint(167, 176)
        return reverse_geo_search(randomlat, randomlong)

    elif region == "N":
        randomlat = random.randint(-90, 90)
        randomlong = random.randint(-180, 180)
        return reverse_geo_search(randomlat, randomlong)

# sets range as latitude longitude range of region, then randoms
    return None


def query(choice):
    '''
    takes all user input for menu
    INPUT: choice = user selection from menu
    OUTPUT: calls functions, prints errors
    '''

    if choice == "latlong":
        print("Please enter your street number followed by your street name, e.g: ")
        streetnumberstreetname = input("118 Walker Street\n")
        #asks for street number and name

        print("Please entre your city followed by your state, e.g: ")
        citystate = input("North Sydney NSW\n")
        #asks for city and state

        if latlong(streetnumberstreetname, citystate) is None:
            print("Error, something went wrong, Check the address!")
            # if returns None, print error, else print the result

        else:
            print(latlong(streetnumberstreetname, citystate))

    elif choice == "location":
        lat = input("Please enter a latitude 0-90\n")
        longitude = input("Please enter a longitude 0-180\n")

        if location(lat, longitude) is None:
            print("Error, something went wrong, Check your values!")

        else:
            print(location(lat, longitude))

    elif choice == "random":
        print("What region would you like to search in?\n")
        region = input("[N] None\n[AUS] Australia\n[NZ] New Zealand\n")
        #user selects region to search in
        if randomloc(region) is None:
            print("Error, we didn't find anything cool, or the region is invalid.")
        else:
            print(randomloc(region))

    elif choice == "exit":
        quit()
    else:
        print("Error: Invalid Selection!")



def gmaps_menu():
    '''
    Prints the menu for GeoCode.py
    '''




    parser = argparse.ArgumentParser()
    parser.add_argument("--latlong", help="Find the lat/longitude of an address. Requires streetnumberstreetname and citystate", action="store_true")
    parser.add_argument("--location", help="Find the lat/longitude of an address. Requires lat and longitude", action="store_true")
    parser.add_argument("--random", help="Generates a random location, requires a region argument.", action="store_true")
    parser.add_argument("-region", help="Sets the region in which to generate a random location for random(). OPTIONS: [AUS] Australia, [NZ] New Zealand, [N] NONE")
    parser.add_argument("-lat", help="Latitude, ranges from -90 to 90")
    parser.add_argument("-longitude", help="Longitude, ranges from -180 to 180")
    parser.add_argument("-streetnumberstreetname", help="Street number and name, e.g 1600 Amphitheatre Parkway. MAKE SURE TO SURROUND THIS IN QUOTES")
    parser.add_argument("-citystate", help="City and state, e.g Mountain View, California. MAKE SURE TO SURROUND THIS IN QUOTESw")
    args = parser.parse_args()

    if args.location and args.lat and args.longitude:
        print(location(args.lat, args.longitude))

    if args.random and args.region:
        print(randomloc(args.region))

    if args.latlong and args.streetnumberstreetname and args.citystate:
        print(latlong(args.streetnumberstreetname, args.citystate))


    while True:
        print("- - - - - - - - -\nWhat would you like to do?")
        print("[latlong] Converts a location to lat/longitude")
        print("[location] Converts lat/longitude to location.")
        print("[random] Generates a random location\n[Exit] Stops the program")
        choice = input("- - - - - - - - -\n")
        query(choice)



if __name__ == "__main__":
    gmaps_menu()
