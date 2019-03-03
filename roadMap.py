import googlemaps
from datetime import datetime
from math import *

API_KEY = 'AIzaSyCCCe0PzBOkTbuOKfXJcZyJhwwVYfaEP8U'

#returns list of all waypoints at each different turn to make
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

    return all_way_points

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
    town = ''
    state = ''

    for x in range(len(result[0]['address_components'])):
        if ( result[0]['address_components'][x]['types'][0] == 'locality'):
            town = result[0]['address_components'][x]['long_name']
        if ( result[0]['address_components'][x]['types'][0] == 'administrative_area_level_1'):
            state = result[0]['address_components'][x]['short_name']

    full = result[0]['formatted_address']

    town_state = town + " " + state

    return town_state, full


#Take waypoints and divide by the number of days
#Each waypoint will be a different day
def parseWaypoints(waypoints, days):

    total_distance = findDistance(waypoints[0],waypoints[-1])
    w_p = []

    #Parse waypoints based on how far away they are from each other
    current = waypoints[0]

    for i in range(len(waypoints)-1):
        dist = findDistance(waypoints[i],waypoints[i+1])
        dist_temp = findDistance(current,waypoints[i+1])

        if dist > (total_distance / days):
            w_p.append(waypoints[i+1])
            current = waypoints[i+1]

        elif dist_temp > (total_distance / days):
            w_p.append(waypoints[i+1])
            current = waypoints[i + 1]

    w_p.append(waypoints[-1])

    return w_p