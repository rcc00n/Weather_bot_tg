import requests
import json
from urllib.parse import quote
from utils import SingletonCounter
api_key = "bf0a20c083fcba8ec90f9c04628badd3"  # open weather map token (5 days/3 hours free subscription)
# getting data from OpenWeatherMap

def wind_direction(deg):
    if 23 <= deg < 68:
        return 'Северо-восток'
    elif 68 <= deg < 113:
        return 'Восток'
    elif 113 <= deg < 158:
        return 'Юго-восток'
    elif 158 <= deg < 203:
        return 'Юг'
    elif 203 <= deg < 248:
        return 'Юго-запад'
    elif 248 <= deg < 293:
        return 'Запад'
    elif 293 <= deg < 338:
        return 'Северо-запад'
    else:
        return 'Северный'



def get_weather(city, api_key):
    counter = SingletonCounter()
    city = quote(city)  # URL encoding for city
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    counter.request_counter += 1
    return data

def weather_replace(weather):
    with open("Data/weather.json", "r", encoding="utf-8") as file:
        weather_translations = json.load(file)

    for key in weather_translations:
        weather = weather.replace(key, weather_translations[key])

    return weather


def parse_weather_data(data, l_border, r_border, city):
    forecast = ''
    for i in range(l_border, r_border):
        item = data['list'][i]

        date = item["dt_txt"]
        weather = weather_replace(item['weather'][0]['description'])
        temperature = round(item['main']['temp'] - 273.15)
        wind_speed = item['wind']['speed']
        wind_deg = item['wind']['deg']
        pressure1 = item["main"]["pressure"]
        pressure2 = round(pressure1 * 0.75006156, 2)
        humidity = item["main"]["humidity"]
        wind_dir = wind_direction(wind_deg)

        forecast_fields = {
            "date": date,
            "weather": weather,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": f"{pressure1} гПа, {pressure2} мм рт ст",
            "wind_speed": wind_speed,
            "wind_direction": wind_dir,
        }

        forecast += '\n'.join(f"{key}: {value}" for key, value in forecast_fields.items()) + '\n\n'

    return forecast

