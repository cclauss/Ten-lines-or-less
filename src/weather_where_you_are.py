import geocoder
import requests

HTTP_STATUS_OK = 200
loc = geocoder.ip("me").json  # Resolves location by IP
city_country = f"{loc['city']},{loc['country']}"  # City string for URL
APPID = "beb97c1ce62559bba4e81e28de8be095"
weather = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?APPID={APPID}&q={city_country}"
).json()
if weather.get("cod") == HTTP_STATUS_OK:
    print(
        f"Weather in {city_country}\n------\n"
        + "\n".join(f"{key}: {value}" for key, value in weather.items())
    )
else:
    print("Error fetching data.")
