from voice import voice
from handlers import get_weather, laugh, get_walk, get_temperature, get_wind
import random

commands = [
    {'id': 0, 'text': 'анекдот', 'handler': laugh}, 
    {'id': 1, 'text': 'погод', 'handler': get_weather},
    {'id': 2, 'text': 'прогулк', 'handler': get_walk},
    {'id': 3, 'text': 'температура', 'handler': get_temperature},
    {'id': 4, 'text': 'ветер', 'handler': get_wind}

]
activation = "апельсин"

class Command:
    def __init__(self, text):
        self.text = text
        self.map()

    def map(self):
        if self.text.startswith(activation):
            self.text = self.text.replace(activation, '').strip()
            for cmd in commands:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech(random.choice(['Давайте лучше о погоде',
                                                    'Не понял, Вы о чем?',
                                                    'Повторите еще раз',
                                                    'Да не знаю я такую команду']))

    def run(self, cmd):
        handler = cmd['handler']
        handler(self.text)


