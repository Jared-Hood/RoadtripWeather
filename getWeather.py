import requests
def getWeather(lat, long):
    try:
        api_address1 = 'http://api.openweathermap.org/data/2.5/forecast?appid=3529eeb526092717a618e922c6b3d4bd&lat='
        url = api_address1 + lat + '&lon=' + long
        data = []
        json_data = requests.get(url).json()
        #print(json_data)
        data = []
        data.append(json_data['city']['name'])
        daysforecast = []
        max = 0
        min = 10000000
        for day in json_data['list']:
            info = []
            if int(day['main']['temp_min']) < min:
                min = int(day['main']['temp_min'])
            if int(day['main']['temp_max']) > max:
                max = int(day['main']['temp_max'])
            if json_data['list'].index(day) % 8 == 0:
                info.append((9 * (min - 273) / 5) + 32)
                info.append((9 * (max - 273) / 5) + 32)
                info.append(day['weather'][0]['main'])
                info.append(day['weather'][0]['description'])
                info.append(day['dt_txt'])
                data.append(info)
                max = 0
                min = 10000000
        return data

    except:
       print("City not found")




