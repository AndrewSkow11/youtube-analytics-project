from src.youtube_api import get_service


class Video:
    def __init__(self, video_id):
        self.video_id = video_id

        youtube = get_service()
        video_response = youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=self.video_id).execute()

        # название
        self.video_title: str = video_response['items'][0]['snippet']['title']
        # получить id можно из адреса видео
        # ссылка
        self.video_link: str = (
                "https://www.youtube.com/watch?v=" + self.video_id)
        self.view_count: int = \
            video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = \
            video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
