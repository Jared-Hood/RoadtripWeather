import googlemaps
from datetime import datetime
from math import *

API_KEY = 'AIzaSyCCCe0PzBOkTbuOKfXJcZyJhwwVYfaEP8U'

def getDirections(start,end):
    gmaps = googlemaps.Client(key='AIzaSyCCCe0PzBOkTbuOKfXJcZyJhwwVYfaEP8U')
    now = datetime.now()

    directions = gmaps.directions(start,end)

    all_way_points = []

    for leg in directions[0]['legs']:
        startAddress = leg['start_address']
        steps = leg['steps']
        for i in steps:
            coords = i['end_location']
            lat = coords['lat']
            lng = coords['lng']
            point = (lat,lng)
            all_way_points.append(point)

    w_p = []

    #Parse waypoints based on how far away they are from each other
    current = all_way_points[0]
    for i in range(len(all_way_points)-1):
        if i == 0:
            w_p.append(all_way_points[0])
        else:
            dist = findDistance(all_way_points[i],all_way_points[i+1])
            dist_temp = findDistance(current,all_way_points[i+1])
            if dist > 50:
                w_p.append(all_way_points[i+1])
                current = all_way_points[i+1]
            elif dist_temp > 50:
                w_p.append(all_way_points[i+1])
                current = all_way_points[i + 1]
    w_p.append(all_way_points[-1])

    return w_p

#Find the distance between 2 given coordinates
def findDistance(c1, c2):
    lat1 = radians(c1[0])
    lon1 = radians(c1[1])
    lat2 = radians(c2[0])
    lon2 = radians(c2[1])
    dist = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    return dist

#Get the location name of a particular lat, long coordinate
#Returns the town, state and the full address
def reverseGeo(c):
    gmaps = googlemaps.Client(key='AIzaSyCCCe0PzBOkTbuOKfXJcZyJhwwVYfaEP8U')
    result = gmaps.reverse_geocode(c)

    town = result[0]['address_components'][2]['long_name']
    state = result[0]['address_components'][4]['short_name']
    country = result[0]['address_components'][5]['short_name']
    full = result[0]['formatted_address']

    town_state = town + ", " + state

    return town_state, full

start = "University of Virginia, VA"
end = "Clifton, VA"

x = getDirections(start,end)
y, z = reverseGeo(x[2])
print(y)
print(z)
print(x)

#2,4,5