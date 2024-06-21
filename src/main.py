class Controller():
    def __init__(self):
        self.__MAX_FRAMES = 5
        self.__fileLoader = FileLoader

    def run(self, frames):
        frames = self.__fileLoader.load('videoTesting.mp4')