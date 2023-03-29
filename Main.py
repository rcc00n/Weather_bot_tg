import requests
import json
import telebot
from telebot import types
from time import *
from colorama import init, Fore

# from colorama import Back
# from colorama import Style

init(autoreset=True)  # for colorama

global i

l_border = 1  # default left border of measurements number (new measurement each 3 hour)
r_border = 11  # default right border of measurements number (new measurement each 3 hour)

bot = telebot.TeleBot("5839014213:AAE568cbq_VI8XXgY3nBEIBEu2s7meH5vPk")  # bot 2
api_key = "bf0a20c083fcba8ec90f9c04628badd3"  # open weather map token (5 days/3 hours free subscription)

# writing cities that work in the bot
cities = {
    "Сочи": "Sochi, RU",
    "Анапа": "Anapa, RU",
    "Новороссийск": "Novorossiysk, RU",
    "Севастопольская бухта": "Sevastopol, UA",
    "Балаклава": "Balaklava, UA",
    "Кача": "Kacha, UA",
    "Широкая Балка": "Shirokaya Balka, RU",
    "Ялта": "Yalta, UA",
    "Мыс Толстяк": "Северная сторона, UA",
    "Голубая бухта": "Казачья бухта, UA",
    "Форос": "Foros, UA",
    "Парк Победы": "Sevastopol, UA",
    "Фрунзе": "Frunze, UA",
    "Песчанное": "Uglovoye, UA",
    "Алушта": "Alushta, UA",
    "Арабатская Стрелка": "Urochyshche Rozhkova, UA",
    "Камышовая бухта": "Shablykina, UA",
    "Немецкая балка": "Kacha, UA",
    "Фиолент": "Balaklava, UA",
    "Ласпи": "Laspi, UA",
    "Учкуевка": "Казачья бухта, UA",
    "Инжир": "Balaklava, UA",

}


# start command and func
@bot.message_handler(commands=['start'])  # start command
def start(message):  # start func

    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + "/start", "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))

    bot.reply_to(message,  # replying to user's message instead of just sending a message
                 f'Привет, {message.from_user.first_name} ! Я бот для показа погоды.'  # text inside the reply
                 f' Для помощи напишите /help')


# help command and func
@bot.message_handler(commands=['help'])  # help command
def start_message(message):  # help func
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + "/help", "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))
    bot.reply_to(message,  # replying to user's message instead of just sending a message
                 f'Я умею показывать погоду около вашего дома! \n\n'  # text inside the reply
                 f' 1. Введите слово /weather1 и выберите Ваш город для прогноза на сегодня.\n'
                 f' 2.  Введите слово /weather2 и выберите Ваш город для прогноза на завтра.\n'
                 f' 3. Введите слово /weather35 и выберите Ваш город для прогноза с третьего по пятый дни.\n\n'
                 f'Для связи с моим создателем по любым вопросам обратитесь к https://t.me/Rac_c00n. \n\n'
                 f' Что то еще {message.from_user.first_name} ?')


# getting data from OpenWeatherMap
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"  # url with params city and api_key
    response = requests.get(url)
    data = json.loads(response.text)
    return data


@bot.message_handler(commands=['weather1'])
def days1(message):
    global l_border, r_border
    l_border = 0
    r_border = 10
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    for city in cities.keys():
        markup.add(city)
    bot.send_message(message.chat.id, "Пожалуйста, выберите вашу локацию:", reply_markup=markup)
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + "/weather1", "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))

    return l_border, r_border


@bot.message_handler(commands=['weather2'])
def days2(message):
    global l_border, r_border
    l_border = 10
    r_border = 20
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    for city in cities.keys():
        markup.add(city)
    bot.send_message(message.chat.id, "Пожалуйста, выберите вашу локацию:", reply_markup=markup)
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + "/weather2", "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))

    return l_border, r_border


# beget server
@bot.message_handler(commands=['weather35'])
def days35(message):
    global l_border, r_border
    l_border = 20
    r_border = 40
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    for city in cities.keys():
        markup.add(city)
    bot.send_message(message.chat.id, "Пожалуйста, выберите вашу локацию:", reply_markup=markup)
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + "/weather35", "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))

    return l_border, r_border


def parse_weather_data(data):
    global l_border, r_border
    forecast = ""
    for i in range(l_border, r_border):
        if i % 2 == 0:
            date = data["list"][i]["dt_txt"]
            weather = data["list"][i]["weather"][0]["description"]
            temperature = data["list"][i]["main"]["temp"] - 273.15
            pressure = data["list"][i]["main"]["pressure"]
            humidity = data["list"][i]["main"]["humidity"]
            wind_speed = data["list"][i]["wind"]["speed"]
            wind_gusts = data["list"][i]["wind"]["gust"]
            wind_direction_degrees = data["list"][i]["wind"]["deg"]
            wind_direction = ""

            # wind
            if 337.5 <= wind_direction_degrees <= 360 or 0 <= wind_direction_degrees < 22.5:
                wind_direction = "Северный⬇"
            elif 22.5 <= wind_direction_degrees < 67.5:
                wind_direction = "Северо-Восточный↙"
            elif 67.5 <= wind_direction_degrees < 112.5:
                wind_direction = "Восточный⬅"
            elif 112.5 <= wind_direction_degrees < 157.5:
                wind_direction = "Юго-Восточный↖"
            elif 157.5 <= wind_direction_degrees < 202.5:
                wind_direction = "Южный⬆"
            elif 202.5 <= wind_direction_degrees < 247.5:
                wind_direction = "Юго-Западный↗"
            elif 247.5 <= wind_direction_degrees < 292.5:
                wind_direction = "Западный➡"
            elif 292.5 <= wind_direction_degrees < 337.5:
                wind_direction = "Северо-Западный↘"

                # sky condition

            # thunderstorm
            weather = weather.replace("thunderstorm with light rain", "Гроза с небольшим дождем⛈")
            weather = weather.replace("thunderstorm with rain", "Гроза с дождем⛈")
            weather = weather.replace("thunderstorm with heavy rain", "Гроза с сильным дождем⛈")
            weather = weather.replace("light thunderstorm", "Легкая гроза⛈")
            weather = weather.replace("thunderstorm", "Гроза⛈")
            weather = weather.replace("heavy thunderstorm", "Сильная гроза⛈")
            weather = weather.replace("ragged thunderstorm", "Местами гроза⛈")
            weather = weather.replace("thunderstorm with light drizzle", "Гроза с мелким дождем⛈")
            weather = weather.replace("thunderstorm with drizzle", "Гроза с моросью⛈")

            # drizzle
            weather = weather.replace("light intensity drizzle", "Мелкая морось💧")
            weather = weather.replace("drizzle", "Морось💧")
            weather = weather.replace("heavy intensity drizzle", "Сильная морось💧💧")
            weather = weather.replace("light intensity drizzle rain", "Слабая морось💧")
            weather = weather.replace("drizzle rain", "Моросящий дождь🌧")
            weather = weather.replace("heavy intensity drizzle rain", "Ливень🌧")
            weather = weather.replace("shower rain and drizzle", "Ливень🌧")
            weather = weather.replace("heavy shower rain and drizzle", "Ливень🌧")
            weather = weather.replace("shower drizzle", "Очень сильный дождь🌧")

            # rain
            weather = weather.replace("light rain", "Легкий дождь🌧")
            weather = weather.replace("moderate rain", "Умеренный дождь🌧")
            weather = weather.replace("heavy intensity rain", "Сильный интенсивный дождь🌧")
            weather = weather.replace("very heavy rain", "Очень сильный дождь🌧")
            weather = weather.replace("extreme rain", "Сильный дождь🌧")
            weather = weather.replace("freezing rain", "Ледяной дождь")
            weather = weather.replace("light intensity shower rain", "Слабый ливень🌧")
            weather = weather.replace("shower rain", "Ливневый дождь🌧")
            weather = weather.replace("heavy intensity shower rain", "Сильный ливневый дождь🌧")
            weather = weather.replace("ragged shower rain", "Прерывистый ливень🌧")

            # snow
            weather = weather.replace("light snow", "Слабый снег❄")
            weather = weather.replace("snow", "Снег❄")
            weather = weather.replace("Heavy snow", "Сильный снег❄")
            weather = weather.replace("Sleet", "Мокрый снег❄")
            weather = weather.replace("Light shower sleet", "Слабый снегопад, мокрый снег❄")
            weather = weather.replace("Shower sleet", "Снегопад, мокрый снег❄")
            weather = weather.replace("Light rain and snow	", "Слабый дождь со снегом❄")
            weather = weather.replace("Rain and snow", "Дождь со снегом❄")
            weather = weather.replace("Light shower snow", "Слабый снегопад❄")
            weather = weather.replace("Shower snow", "Снегопад❄")
            weather = weather.replace("Heavy shower snow", "Сильный снегопад❄")

            # atmosphere
            weather = weather.replace("mist", "Туман🌫")
            weather = weather.replace("smoke", "Дым🌫")
            weather = weather.replace("Haze", "Туман🌫")
            weather = weather.replace("sand/ dust whirls", "песчаные/пылевые вихри💨")
            weather = weather.replace("fog", "Туман🌫")
            weather = weather.replace("sand", "Ветер с песком💨")
            weather = weather.replace("dust", "Пыльный ветер💨")
            weather = weather.replace("volcanic ash", "Вулканический пепел🌫")
            weather = weather.replace("squalls", "Шквальный ветер💨")
            weather = weather.replace("tornado", "Торнадо💨")

            # not done yet
            weather = weather.replace("clear sky", "Ясное небо☀")
            weather = weather.replace("few clouds", "Малооблачно⛅")
            weather = weather.replace("scattered clouds", "Рассеянные облака🌤")
            weather = weather.replace("broken clouds", "Дождевые облака☁")
            weather = weather.replace("overcast clouds", "Грозовые облака☁")

            forecast += f"{date}\n\nПогода: {weather}\nТемпература: {int(round(temperature)):.2f} (°C) \nДавление: {pressure} (гПа) \nВлажность: {humidity} (%) \nВетер: {wind_speed} (м/с) \nПорывы до: {wind_gusts} (м/с) \nНаправление ветра: {wind_direction}\n\n"
    return forecast


def handle_message(message, city, api_key):
    data = get_weather(city, api_key)
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + str(city), "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))

    return parse_weather_data(data)


@bot.message_handler(func=lambda message: message.text in cities.keys())
def handle_city(message):
    response = handle_message(message, cities[message.text], api_key)
    bot.reply_to(message, response)


bot.polling(none_stop=True)
