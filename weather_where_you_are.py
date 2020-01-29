import location, requests, speech

loc = location.reverse_geocode(location.get_location())
city_country = "{City},{Country}".format(**loc[0])
print(f"Weather in {city_country}:")
url = ("http://api.openweathermap.org/data/2.5/weather?"
       "APPID=beb97c1ce62559bba4e81e28de8be095&q=")
weather = requests.get(url + city_country).json()
for key, value in weather.items():
    print(f"{key}: {value}")
speech.say(f"It is currently {weather['weather'][0]['main']} in {city_country}.")
