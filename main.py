import googleImages
import roadMap
import getWeather

start = "Paris"
end = "Berlin"
days = 5

directions = roadMap.getDirections(start,end)
parsed_directions = roadMap.parseWaypoints(directions,days)
city_state, full_address = roadMap.reverseGeo(parsed_directions[1])

iter = 0
for i in range(len(parsed_directions)):
    lat = str(parsed_directions[i][0])
    long = str(parsed_directions[i][1])
    currentWeather = getWeather.getWeather(lat, long)[1][2]

    city_state, full_address = roadMap.reverseGeo(parsed_directions[iter])
    googleImages.getPics(city_state + " " + currentWeather)
    iter += 1

    print(currentWeather + ": " + city_state)

