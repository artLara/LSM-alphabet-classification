import sys
sys.path.append('../../')
from src.FileLoader import FileLoader

class FR1():
    def __init__(self):
        self.__path = '../media/'

    def run4image(self):
        print('#######Image loader test#############')
        fl = FileLoader()
        frames = fl.load(self.__path+'imageTesting.jpg')
        print('Len:{}'.format(len(frames)))
        print('Shape:{}'.format(frames[0].shape))

    def run4video(self):
        print('#######Video loader test#############')
        fl = FileLoader()
        frames = fl.load(self.__path+'videoTesting.mp4')
        print('Len:{}'.format(len(frames)))
        print('Shape:{}'.format(frames[0].shape))


fr = FR1()
fr.run4image()
fr.run4video()
