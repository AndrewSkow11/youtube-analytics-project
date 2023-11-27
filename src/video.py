from src.youtube_api import get_service


## Описание задачи

# __Проблема:__ при инициализации экземпляра класса `Video`
# пользователь может передать несуществующий id видео.
#
# Внедрите в код блоки `try/except` , чтобы обработать такую ситуацию.
#
# Если пользователь передал id,
# с которым невозможно получить данные о видео по API,
# то у экземпляра инициализируется только свойство `video_id`,
# а остальные поля принимают значение `None`.
#


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None

        youtube = get_service()

        try:
            video_response = youtube.videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=self.video_id).execute()
            self.title: str = video_response['items'][0]['snippet']['title']
            self.video_link: str = (
                    "https://www.youtube.com/watch?v=" + self.video_id)
            self.view_count: int = \
                video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = \
                video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            print("Не нашлось видео с таким id")
            self.title = None
            self.video_link = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
