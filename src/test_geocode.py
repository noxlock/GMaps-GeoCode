'''
Script to test four functions of geocody.py
tests two conversion functions, 
and two error handling functions
Author: noxlock
'''

from geocode import latlong, reverse_geo_search, is_int, is_float

# TEST 1

def test_latlong():
    '''
    tests that latlong returns the desired result
    '''

    assert latlong("1600 Amphitheatre Parkway", "Mountain View, CA 94043, USA") == {'lat': 37.4208484, 'lng': -122.08552}
    assert latlong("118 Walker St", "North Sydney NSW 2060, Australia") == {'lat': -33.83777070000001, 'lng': 151.2088326}


def test_reverse_geo_search():
    '''
    tests that latlong returns the opposite result of latlong
    '''

    assert reverse_geo_search(37.4208484, -122.08552) == "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
    assert reverse_geo_search(-33.83777070000001, 151.2088326) == "118 Walker St, North Sydney NSW 2060, Australia"

# the two functions above test that geocoding works correctly, and returns the same result if you swap
# between latlong and reverse_geo_search

# TEST 2

def test_is_int():
    '''
    tests that is_int checks values correctly
    '''

    assert is_int(3, 45) == True
    assert is_int(3, "$") == False

def test_is_float():
    '''
    tests that is_float checks values correctly
    '''
    assert is_float(3.1, 33) == True
    assert is_float("/", 33.3) == False

# the two functions above test that some of the error handling works correctly