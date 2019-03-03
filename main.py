import googleImages
import roadMap
import getWeather

start = "Portland OR"
end = "Mexico"
days = 5

directions = roadMap.getDirections(start,end)
parsed_directions = roadMap.parseWaypoints(directions,days)
city_state, full_address = roadMap.reverseGeo(parsed_directions[1])

print(parsed_directions)
iter = 1
for i in range(len(parsed_directions)):
    lat = str(parsed_directions[i][0])
    long = str(parsed_directions[i][1])
    currentWeather = getWeather.getWeather(lat, long)[iter][2]

    city_state, full_address = roadMap.reverseGeo(parsed_directions[i])
    googleImages.getPics(city_state + " " + currentWeather + " day")
    iter += 1

    print(currentWeather + ": " + city_state)