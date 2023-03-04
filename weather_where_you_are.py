import location
import requests
import speech

loc = location.reverse_geocode(location.get_location())
city_country = "{City},{Country}".format(**loc[0])
print(f"Weather in {city_country}:")
APPID = "beb97c1ce62559bba4e81e28de8be095&q="
URL = f"http://api.openweathermap.org/data/2.5/weather?APPID={APPID}&q="
weather = requests.get(URL + city_country).json()
print("\n".join(f"{key}: {value}" for key, value in weather.items()))
speech.say(f"It is currently {weather['weather'][0]['main']} in {city_country}.")
