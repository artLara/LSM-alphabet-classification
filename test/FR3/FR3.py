import sys
sys.path.append('../../')
sys.path.insert(0, '/home/lara/Documents/lsm/LettersPapper/LSM-alphabet-classification/src')
from src.FileLoader import FileLoader
from src.Hand import Hand
from src.HandsDetectorMP import HandsDetector
from src.StaticSignClassifier import StaticSignClassifier

class FR1():
    def __init__(self):
        self.__path = '../media/'
        self.__handsDetector = HandsDetector()
        self.__classifier = StaticSignClassifier()

    def run(self, fileName):
        fl = FileLoader()
        frames = fl.load(self.__path+fileName)
        notDetected = 0
        detected = 0
        letters = []
        for frame in frames:
            hand  = self.__handsDetector.detect(frame)
            if hand != None:
                landmarks = hand.getLandmarksNormalized() 
                letter, sm_value = self.__classifier.classify(landmarks)
                letters.append(letter)
                detected += 1
                
            else:
                notDetected += 1

        print('Total frames:{}'.format(len(frames)))
        print('Detected:{}'.format(detected))
        print('Not detected:{}'.format(notDetected))
        print('Len:{}'.format(len(letters)))
        print('Info:{}'.format(letters))


fr = FR1()
print('#######Image preprocessing test#############')
fr.run('imageTesting.jpg')

print('\n#######Video preprocessing test#############')
fr.run('videoTesting.mp4')
