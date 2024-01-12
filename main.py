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
    celcius = kelvin - 273.15
    return celcius, fahrenheit

response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celcius, temp_fahrenheit = tempConversion(temp_kelvin)

temp_kelvin = response['main']['feels_like']
feels_like_temp_celcius, feels_like_temp_fahrenheit = tempConversion(feels_like_temp_kelvin)
print(response)