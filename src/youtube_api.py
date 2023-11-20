from googleapiclient.discovery import build
import os

# третью домашку оставляю без изменений, так как там нужен
# get_service() как статический метод

def get_service():
    """класс-метод `get_service()`, возвращающий объект для работы
     с YouTube API"""
    youtube = build('youtube', 'v3',
                    developerKey=os.getenv('YT_API_KEY'))
    return youtube


# <googleapiclient.discovery.Resource object at 0x10749d3d0>
# print(get_service())