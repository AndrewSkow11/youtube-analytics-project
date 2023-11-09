import json
import os
from googleapiclient.discovery import build

# проверка переменной окружения
# print(os.getenv('YT_API_KEY'))

# status: home_work_2

# создать специальный объект для работы с API
youtube = build('youtube', 'v3',
                developerKey=os.getenv('YT_API_KEY'))


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = (youtube.channels().list(id=channel_id,
                                                part='snippet,statistics').
                        execute())

        self.info_about_chanel = (
            json.dumps(self.channel, indent=2, ensure_ascii=False))

        self.channel_dict = json.loads(self.info_about_chanel)
        self.channel_snippet = self.channel_dict['items'][0]['snippet']

        # print(self.channel_snippet)

        # - id канала
        self.id = self.channel_dict['items'][0]['id']
        # - название канала
        self.title = self.channel_snippet['title']
        # - описание канала
        self.description = self.channel_snippet['description']
        # - ссылка на канал
        self.url = self.channel_snippet['thumbnails']['default']['url']
        # - количество подписчиков
        self.subscribes = (
            self.channel_dict)['items'][0]['statistics']['subscriberCount']
        # - количество видео
        self.video_count = self.channel_dict['items'][0]['statistics']['videoCount']
        # - общее количество просмотров
        self.views_count = self.channel_dict['items'][0]['statistics']['viewCount']

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





