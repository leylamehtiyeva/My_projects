

class Video:
    """
    To create a video
    """
    def create(self, name):
        self.__name = name

    def play(self):
        print(f'воспроизведение видео {self.__name}')


class Youtube:
    """
    To add and play videos on YouTube
    """
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v1.create('Python')  # create a video named Python
v2 = Video()
v2.create('Python ООП')  # create a video named Python ООП
y = Youtube()
y.add_video(v1)
y.add_video(v2)
y.play(1)





