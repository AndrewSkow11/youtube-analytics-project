import datetime

import isodate

from src.youtube_api import get_service
from src.video import PLVideo

#
# Множественное наследование. Домашнее задание
#
# ## Описание задачи
#
# - Реализуйте класс `PlayList`, который инициализируется _id_ плейлиста и имеет следующие публичные атрибуты:
#   - название плейлиста
#   - ссылку на плейлист
#
# - Реализуйте следующие методы класса `PlayList`
#   - `total_duration` возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста (обращение как к свойству, использовать `@property`)
#   - `show_best_video()` возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
#
# ## Ожидаемое поведение
# - Код в файле `main.py` должен выдавать ожидаемые значения



class PlayList(PLVideo):

    def __init__(self, playlist_id):

        about_playlist = (get_service().playlists().list
                          (id=playlist_id, part='snippet,contentDetails',
                           maxResults=50)
                          .execute())

        # приватный атрибут
        self.__playlist_id = playlist_id

        # публичные атрибуты
        self.title = about_playlist['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id


    @property
    def total_duration(self):
        playlist_videos = (
            get_service()
            .playlistItems().list(playlistId=self.__playlist_id,
                                  part='contentDetails',
                                  maxResults=50,)
            .execute())

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId']
                                for video in playlist_videos['items']]

        video_response = (get_service().videos()
                          .list(part='contentDetails,statistics',
                                                     id=','.join(video_ids)
                                                     ).execute())

        total_duration = datetime.timedelta()

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
            # only for tests in
            # print("duration:", duration)
            # print('total duration', total_duration)

        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста
        (по количеству лайков)"""
        pass


pl1 = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
#