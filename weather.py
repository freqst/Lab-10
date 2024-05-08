import requests
from num2words import num2words as n2w
import random


url = "https://wttr.in/Saint-Petersburg?format=2"
response = requests.get(url)

if response.status_code == 200:
    weather = response.text
weather = weather.split()

emojis = [
    {'id' : 0, 'mood' : "✨", 'text' : "Какое звездное небо!", 'rec' : '1'},
    {'id' : 1, 'mood' : "☁️", 'text' : "Облака белогривые лошадки. Если кратко, то облачно", 'rec' : '1'},
    {'id' : 2, 'mood' : "🌫", 'text' : "Сдувает. Ветренно соответственно", 'rec' : '0'},
    {'id' : 3,'mood' : "🌧", 'text' : "Облака с каплям", 'rec' : '0'},
    {'id' : 4, 'mood' : "🌧", 'text' : "Облака с каплям", 'rec' : '0'},
    {'id' : 5, 'mood' : "❄️", 'text' : "Снежинка.  Снег. Снегопад.", 'rec' : '1'},
    {'id' : 6, 'mood' : "❄️", 'text' : "Снежинка.  Снег. Снегопад.", 'rec' : '1'},
    {'id' : 7, 'mood' : "🌦", 'text' : "Солнце и облака с каплями", 'rec' : '0'},
    {'id' : 8, 'mood' : "🌦", 'text' : "Солнце и облака с каплями", 'rec' : '0'},
    {'id' : 9, 'mood' : "🌧", 'text' : "Опять дождь. Нужен зонт", 'rec' : '0'},
    {'id' : 10, 'mood' : "🌧", 'text' : "Опять дождь. Нужен зонт", 'rec' : '0'},
    {'id' : 11, 'mood' : "🌨", 'text' : "Снегопад", 'rec' : '1'},
    {'id' : 12, 'mood' : "🌨", 'text' : "Снегопад", 'rec' : '1'},
    {'id' : 13, 'mood' : "⛅️", 'text' : "Облачно с прояснениями", 'rec' : '1'},
    {'id' : 14, 'mood' : "☀️", 'text' : "Солнце золотое.", 'rec' : '1'},
    {'id' : 15, 'mood' : "🌩", 'text' : "Гроза без дождя", 'rec' : '0'},
    {'id' : 16, 'mood' : "⛈", 'text' : "Гроза и дождь", 'rec' : '0'},
    {'id' : 17, 'mood' : "⛈", 'text' : "Гроза и дождь", 'rec' : '0'},
    {'id' : 18, 'mood' : "☁️", 'text' : "Облака белогривые лошадки. Если кратко, то облачно", 'rec' : '1'},
]
mood = weather[0]

optionsneg = ['Я бы остался дома',
              'Возможны осадки в виде фрикаделек, берегитесь!',
              'Прогулка на ваше усмотрение'
              ]

optionspos = ['Самое время подышать воздухом',
              'Прогулка еще никому не вредила',
              'Жаль, что я всего лишь голосовой ассистент. Так бы прогулялся',
              'Самое время выйти на улицу'
              ]



for em in emojis:
    if em['mood'] == mood:
        mood_text = em['text']
        rec = em['rec']
        if int(rec) == 1:
            rec = random.choice(optionspos)
            break
        else:
            rec = random.choice(optionsneg)

temperature = n2w(weather[1][2:-2], lang = 'ru')
temperature_num = weather[1][2:-2]
speed_wind = n2w(weather[2][3:-4], lang= 'ru')
speed_wind_num = weather[2][3:-4]

