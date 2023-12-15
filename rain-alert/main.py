import requests
import os
print(os.environ.get("API_KEY"))

# api_key = "b04f2dec3d4b31d0d26c9b8b3208efa5"
# state = 'lagos'
# params = {
#     "lat": 51.507351,
#     "lon": -0.127758,
#     "exclude": "daily,current,minutely",
#     "appid": api_key
# }
# url = f'https://api.openweathermap.org/data/2.5/onecall'
#
# response = requests.get(url, params=params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
# weather_list = [hour_data["weather"][0]["id"] for hour_data in weather_slice]
# print(weather_list)
