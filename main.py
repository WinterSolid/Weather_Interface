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
    farenheit = kelvin * 9/5 - 459.67
    celcius = kelvin - 273.15
    return celcius, farenheit

response = requests.get(url).json()
Kelvin = response['main']['temp']
celc,,temp_farenheit = tempConversion(kelvin)
print(response)