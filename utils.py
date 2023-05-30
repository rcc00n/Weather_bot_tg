import json
import telebot

class SingletonCounter:
    _instance = None
    _request_counter = 0

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(SingletonCounter, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def request_counter(self):
        return self._request_counter

    @request_counter.setter
    def request_counter(self, value):
        self._request_counter = value

def get_cities():
    cities = {}
    try:
        with open("/Data/cities.json", "r") as file:
            cities = json.load(file)
    except Exception as e:
        print(f"Couldn't load cities from file: {e}")

    return cities


def create_markup():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    cities = get_cities()
    if cities:
        for city in cities.keys():
            markup.add(city)
        return markup

