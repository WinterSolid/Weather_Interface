# Import the library
from dotenv import load_dotenv
import datetime as dt
import os
import requests
# Load environment variables from the .env file
load_dotenv()
# Access the API key using os.getenv()
api_key = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "London"
url = BASE_URL + "appid="+ api_key + "&q=" + CITY

#conversions
def tempConversion(kelvin):
    fahrenheit = kelvin * 9/5 - 459.67
    celsius = kelvin - 273.15
    return celsius, fahrenheit

response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = tempConversion(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_temp_celsius, feels_like_temp_fahrenheit = tempConversion(feels_like_kelvin)
wind_speed = response['wind']['speed']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
description = response['weather'][0]['description']
print(f'Temperature in: {CITY} is {temp_fahrenheit: .2f}F / {temp_celsius: .2f}C')
print(f'{CITY} feeels like {feels_like_temp_fahrenheit: .2f}F or {feels_like_temp_celsius: .2f}C')
print(f'Wind speed of {wind_speed}')
