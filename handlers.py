import random
from voice import voice
from weather import mood_text, temperature, speed_wind, rec, temperature_num, speed_wind_num, optionsneg


def get_weather(text):
    voice.text_to_speech(mood_text)
    voice.text_to_speech(f"За окном {temperature} градусафпо цесии")
    voice.text_to_speech(f'Скорость ветра составляет {speed_wind} кэмэ в час') #Ошибки написаны специально для более человеческого произношения

def get_wind(text):
    voice.text_to_speech(f'Скорость ветра составляет {speed_wind} кэмэ в час')

def get_walk(text):
    if 15 < int(speed_wind_num)or int(temperature_num) < 5:
        voice.text_to_speech(random.choice(optionsneg))
    else:
        voice.text_to_speech(rec)


def get_temperature(text):
    voice.text_to_speech(f"За окном {temperature} градусов")


def laugh(text):
    options = [
        'Могу конечно и помолчать. Но не долго. Устаю.',
        'Если деньги зло, то из двух зол я выбираю большее.',
        'Я не просто учусь на своих ошибках… Я постоянно повторяю пройденный материал!',
        'Я никогда не даю советов. И вам не советую.'

    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)

