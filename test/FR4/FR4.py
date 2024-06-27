import sys
sys.path.append('../../')
sys.path.insert(0, '/home/lara/Documents/lsm/LettersPapper/LSM-alphabet-classification/src')
from src.FileLoader import FileLoader
from src.Hand import Hand
from src.HandsDetectorMP import HandsDetector
from src.StaticSignClassifier import StaticSignClassifier
from src.Controller import Controller


class FR1():
    def __init__(self):
        self.__path = '../media/'
        self.__controller = Controller()
        self.__classifier = StaticSignClassifier()

    def run(self, fileName):
        fl = FileLoader()
        frames = fl.load(self.__path+fileName)
        letter = self.__controller.run(frames)
        print('Letter {} detected'.format(letter))


fr = FR1()
print('#######Image preprocessing test#############')
fr.run('imageTesting.jpg')

print('\n#######Video preprocessing test#############')
fr.run('videoTesting.mp4')
