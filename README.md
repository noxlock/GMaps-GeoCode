# Geo<>Code

Geo<>Code is a tool that allows users to convert a location into it's latitude and longitude, and vice versa. Geo<>Code also has a random function, which will print the address of a random location.



## Usage

### Latlong

This command takes a location, and returns a latitude and longitude.

` python3 gmaps.py `

` latlong`

` (street number and street name)`

`(city and state)`



### Location

This command takes two arguments, latitude and longitude, and returns a location.

`python3 gmaps.py`

`location`

`(latitude, longitude) `



### Random Location

This command generates a random location. 

`python3 gmaps.py`

`random`

`(region)`



The Random Location command also takes an optional argument --region:

--region restricts the generation to a given area, e.g:

`random --region AUS`

will only generate a random location within Australia.















