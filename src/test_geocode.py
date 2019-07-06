import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--latlong", help="Find the lat/longitude of an address. Requires streetnumberstreetname and citystate", action="store_true")
    parser.add_argument("--location", help="Find the lat/longitude of an address. Requires lat and longitude", action="store_true")
    parser.add_argument("--random", help="Generates a random location, takes an optional region argument", action="store_true")
    parser.add_argument("--region", help="Sets the region in which to generate a random location for random()")
    parser.add_argument("--lat", help="Latitude, ranges from -90 to 90")
    parser.add_argument("--longitude", help="Longitude, ranges from -180 to 180")


    args = parser.parse_args()

if args.location and args.lat and args.longitude:
    print("les go")
