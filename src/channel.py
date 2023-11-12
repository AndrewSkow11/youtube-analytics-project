import json
import os
from googleapiclient.discovery import build


# home_work 3 status

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.chanel = (Channel.get_service().
                       channels().list(id=channel_id, part='snippet,statistics')
                       .execute())
        self.__channel_id = channel_id

        self.info_about_chanel = (
            json.dumps(self.chanel, indent=2, ensure_ascii=False))

        self.channel_dict = json.loads(self.info_about_chanel)
        self.channel_snippet = self.channel_dict['items'][0]['snippet']

        # - id канала
        self.id = self.channel_dict['items'][0]['id']
        # - название канала
        self.title = self.channel_snippet['title']
        # - описание канала
        self.description = self.channel_snippet['description']
        # - ссылка на канал
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        # - количество подписчиков
        self.subscribes = (
            self.channel_dict)['items'][0]['statistics']['subscriberCount']
        # - количество видео
        self.video_count = self.channel_dict['items'][0]['statistics']
        ['videoCount']
        # - общее количество просмотров
        self.views_count = self.channel_dict['items'][0]['statistics']
        ['viewCount']

    def __str__(self):
        return f'{self.title} {self.url}'

    # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.info_about_chanel)

    # Добавьте в класс `Channel` следующие методы:
    # - класс-метод `get_service()`, возвращающий объект для работы с YouTube API
    @staticmethod
    def get_service():
        """класс-метод `get_service()`, возвращающий объект для работы
         с YouTube API"""
        youtube = build('youtube', 'v3',
                        developerKey=os.getenv('YT_API_KEY'))
        return youtube

    def to_json(self, cls):
        """сохраняет в файл значения атрибутов экземпляра `Channel`"""

        dictionary_of_atr = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribes': self.subscribes,
            'video_count': self.video_count,
            'views_count': self.views_count
        }

        with open('moscowpython.json', 'w') as file:
            json.dump(dictionary_of_atr, file)


    # print(moscowpython + highload)  # 100100
    # print(moscowpython - highload)  # -48300
    # # print(highload - moscowpython)  # 48300
    # # print(moscowpython > highload)  # False
    # # print(moscowpython >= highload)  # False
    # # print(moscowpython < highload)  # True
    # # print(moscowpython <= highload)  # True
    # # print(moscowpython == highload)  # False
    # # новые магисеские методы для перегурузки операторов


    # всё сравнение и матеметические опреации по количеству подписчиков
    def __add__(self, other):
        """operator +"""
        return int(self.subscribes) + int(other.subscribes)

    def __sub__(self, other):
        """operator - """
        return int(self.subscribes) - int(other.subscribes)

    def __lt__(self, other):
        """operator <"""
        return int(self.subscribes) < int(other.subscribes)

    def __le__(self, other):
        """operator <="""
        return int(self.subscribes) <= int(other.subscribes)


    def __eq__(self, other):
        """operator =="""
        return int(self.subscribes) == int(other.subscribes)


    def __gt__(self, other):
        """operator >"""
        return int(self.subscribes) > int(other.subscribes)


    def __ge__(self, other):
        """operator >="""
        return int(self.subscribes) >= int(other.subscribes)
