import requests
import json
import telebot
from time import *
from colorama import init, Fore
from utils import get_cities, create_markup, SingletonCounter
from weather import get_weather, parse_weather_data


init(autoreset=True)

api_key = 'bf0a20c083fcba8ec90f9c04628badd3'
bot = telebot.TeleBot('5839014213:AAE568cbq_VI8XXgY3nBEIBEu2s7meH5vPk')

unique_users = set()


def log_message(message, command):
    current_time = strftime("%a %b %d %H:%M:%S %Y", localtime())
    print(Fore.LIGHTBLUE_EX + command, "спросил:", "ID", Fore.LIGHTGREEN_EX + str(message.from_user.id), "Имя:",
          Fore.LIGHTGREEN_EX +
          str(message.from_user.first_name), "Фамилия:", Fore.LIGHTGREEN_EX +
          str(message.from_user.last_name), "Ник:", Fore.LIGHTGREEN_EX +
          str(message.from_user.username), '////', Fore.LIGHTRED_EX + str(current_time))


@bot.message_handler(commands=['start'])
def start(message):
    log_message(message, "/start")
    bot.reply_to(message,
                 f'Привет, {message.from_user.first_name} ! Я бот для показа погоды.'
                 f' Для помощи напишите /help')


@bot.message_handler(commands=['help'])
def help_message(message):
    log_message(message, "/help")
    bot.reply_to(message,
                 f'Я умею показывать погоду около вашего дома! \n\n'
                 f' 1. Введите слово /weather1 и выберите Ваш город для прогноза на сегодня.\n'
                 f' 2. Введите слово /weather2 и выберите Ваш город для прогноза на завтра.\n'
                 f' 3. Введите слово /weather35 и выберите Ваш город для прогноза с третьего по пятый дни.\n\n'
                 f'Для связи с моим создателем по любым вопросам обратитесь к https://t.me/Rac_c00n. \n\n'
                 f' Что то еще {message.from_user.first_name} ?')




def handle_message(message, city, api_key, l_border, r_border):
    data = get_weather(city, api_key)
    return parse_weather_data(data, l_border, r_border, city)


@bot.message_handler(commands=['weather1', 'weather2', 'weather35'])
def handle_weather_commands(message):
    counter = SingletonCounter()
    l_border, r_border = {
        'weather1': (0, 10),
        'weather2': (10, 20),
        'weather35': (20, 40),
    }[message.text[1:]]
    unique_users.add(message.from_user.id)

    markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True, selective=True)
    cities = get_cities()
    if cities:
        for city in cities.keys():
            markup.add(city)

    bot.send_message(
        message.chat.id, "Пожалуйста, выберите вашу локацию:", reply_markup=markup)

    log_message(message, message.text)

    print(f"\nUnique users: {len(unique_users)}")
    print(f"Request amount: {counter.request_counter}\n")

    bot.register_next_step_handler(message, process_city, l_border, r_border)


def process_city(message, l_border, r_border):
    cities = get_cities()
    if message.text not in cities:
        bot.send_message(
            message.chat.id, "Пожалуйста, выберите город из предложенных вариантов.")
        markup = create_markup()
        bot.send_message(
            message.chat.id, "Пожалуйста, выберите вашу локацию:", reply_markup=markup)
        bot.register_next_step_handler(
            message, process_city, l_border, r_border)
        return

    city = cities[message.text]
    forecast = handle_message(message, city, api_key, l_border, r_border)
    bot.send_message(message.chat.id, forecast)


if __name__ == '__main__':
    bot.polling(none_stop=True)
