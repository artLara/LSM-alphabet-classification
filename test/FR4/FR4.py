import sys
sys.path.append('../../')
sys.path.insert(0, '/home/lara/Documents/lsm/LettersPapper/LSM-alphabet-classification/src')
from src.FileLoader import FileLoader
from src.Controller import Controller


class FR1():
    def __init__(self):
        self.__path = '../media/'
        self.__controller = Controller()

    def run(self, fileName):
        fl = FileLoader()
        frames = fl.load(self.__path+fileName)
        letter = self.__controller.run(frames, verbose=False)
        print('Letter {} detected'.format(letter))


fr = FR1()
print('#######Image A preprocessing test#############')
fr.run('imageTesting.jpg')

print('\n#######Video LL preprocessing test#############')
fr.run('videoTesting_LL.mp4')

print('\n#######Video K preprocessing test#############')
fr.run('videoTesting_k.mp4')

print('\n#######Video RR preprocessing test#############')
fr.run('videoTesting.mp4')
