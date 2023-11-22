import datetime
import isodate
from src.youtube_api import get_service

class PlayList:
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

        # для других методов

        playlist_videos = (
            get_service()
            .playlistItems().list(playlistId=self.__playlist_id,
                                  part='contentDetails',
                                  maxResults=50, )
            .execute())

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId']
                                for video in playlist_videos['items']]

        self.video_response = (get_service().videos()
                               .list(part='contentDetails,statistics',
                                     id=','.join(video_ids)
                                     ).execute())

    @property
    def total_duration(self):

        total_duration = datetime.timedelta()

        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += (datetime.
                               timedelta(seconds=duration.total_seconds()))

        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста
        (по количеству лайков)"""

        max_likes = 0
        id_best_video = ''

        for video in self.video_response['items']:

            like_count = int(video['statistics']['likeCount'])
            print("like_count", like_count)

            if like_count > max_likes:
                max_likes = like_count
                id_best_video = video['id']

        return "https://youtu.be/" + id_best_video
