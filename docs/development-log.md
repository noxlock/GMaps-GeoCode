# Development Log for A2 Coder Academy

## 27/06/19

Was deciding between working on either:

- Google Maps Geocoding

- Catchphrase Generator



Decided on a project named "Phrasegen" or "Quotegen", which takes a list of 150 quotes, splices and joins them, I decided this as I had never worked with an API before, and it sounded difficult. Created a Trello board, made the program functional, made a basic README and flowchart, and pushed to git.



I plan to make arguments for the amount of quotes the program will use.



## 28/06/19

### STATUS UPDATE



Had trouble coming up with a user story for Phrasegen, as it was purely meant for fun. 

Conducted some research on using Google's API, which was my original idea. I then decided to scrap the Phrasegen project and begin work on Geo<>Code, a program which allows for random location generation, and location to geo code conversion.



Today was mainly fooling around, trying to figure out how the API exports its data, and figuring out how to make it readable, I had a lot of trouble with this, as I initially thought it was a JSON, turns out it was actually classified as a list of dictionaries, I had no idea how to iterate this so I got some help from a forum.



## 29/06/19

Completed:

- menu

- error handling

- lat/longitude to location

- location to lat/long

- fixed IndexError

- fixed casting

  

To do:

- checking if value is greater or less than

Added menu, error handling, lat/longitude to location, and location to lat/longitude functions.

Fixed IndexError when trying to check if list is empty.

Began work on rewriting error handling, had trouble with casting, managed to get it solved by the end of the day. I hope to fix checking if a value is greater or less than as it's ignoring the check and giving me a HTTP error.



## 30/06/19

Complete:

- rewrote error handling
- is_greater (greater or less than check)

Completely rewrote single error handling function into many, smaller functions to make it easier to pinpoint errors. Fixed is_greater function, it was missing an elif, which caused it to return True if one check passed, but not the other. 

**Latitude to location is now completely functional.**



## 4/07/19

Complete:

- rewrote latlong and reverse_geo_search, now down to ~3 lines

- linted to 10 points

- random function, now works with region.

  

To do:

- lots of documentation
- args



## 5/07/19

Complete

- some documentation

- fully working random()

- args

- **program is done**

  

To do:

- lots more documentation
- readme
- testing
- clean up documentation that i've already done