# This code calculates the distance between two places inputed by the user

import geopy.distance

# get input from user
place1 = input("Enter first place: ")
place2 = input("Enter second place: ")

# get coordinates of places
coord1 = geopy.geocoders.Nominatim(user_agent="my_app").geocode(place1).point
coord2 = geopy.geocoders.Nominatim(user_agent="my_app").geocode(place2).point

# calculate distance between places
distance = geopy.distance.distance(coord1, coord2).km

# print distance
print(f"The distance between {place1} and {place2} is {distance:.2f} km")