import json
import os
from googleapiclient.discovery import build

# проверка переменной окружения
# print(os.getenv('YT_API_KEY'))

# создать специальный объект для работы с API
youtube = build('youtube', 'v3',
                developerKey=os.getenv('YT_API_KEY'))

# проверка созданного специального объекта
# print(youtube)




class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = (youtube.channels().list(id=channel_id,
                                               part='snippet,statistics').
                        execute())


    # def printj(dict_to_print: dict) -> None:
    #     """Выводит словарь в json-подобном удобном формате с отступами"""
    #     print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


