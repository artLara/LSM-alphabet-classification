import sys
sys.path.append('../../')
sys.path.insert(0, '/home/lara/Documents/lsm/LettersPapper/LSM-alphabet-classification/src')
from src.FileLoader import FileLoader
from src.Controller import Controller
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
import numpy as np
import string

class FR6():
    def __init__(self):
        self.__path = '../media/'
        self.__controller = Controller()
        self.__fl = FileLoader()
        self.__targets = ['k', 'll', 'rr']

    def run(self):
        notDetected = []
        y_true = []
        y_pred = []
        m = {}
        lettersList = list(string.ascii_lowercase)
        lettersList.remove('k')
        lettersList += self.__targets

        for i in lettersList:
            m[i] = {}
            for j in lettersList:
                m[i][j] = 0

        for target in self.__targets:
            for i in range(100):
                frames = self.__fl.load(self.__path+'{}/{}{}.mp4'.format(target,target, i))
                letter = self.__controller.run(frames, verbose=False)
                if letter == '-':
                    notDetected.append('{}{}.mp4'.format(target,i))
                    print('Did not hands detect in Video {}{}.mp4'.format(target,i))
                    continue

                y_pred.append(letter)
                y_true.append(target)
                print('y_pred:{}'.format(letter))
                try:
                    m[letter][target] += 1
                except:
                    continue

        print(m)
        score = f1_score(y_true, y_pred, average="macro")
        print("F1-Score: ", score)
        score = precision_score(y_true, y_pred, average="macro")
        print("Precision-Score: ", score)
        score = recall_score(y_true, y_pred, average="macro")
        print("Recall-Score: ", score)
        score = accuracy_score(y_true, y_pred)
        print("Accuracy-Score: ", score)
        print('Hands did not detect in {} videos:'.format(len(notDetected)))
        print(notDetected)

        # print('Total frames:{}'.format(len(frames)))
        # print('Detected:{}'.format(detected))
        # print('Not detected:{}'.format(notDetected))
        # print('Len:{}'.format(len(letters)))
        # print('Info:{}'.format(letters))


fr = FR6()
print('#######Metrics and confussion matrix of dynamic signs#############')
fr.run()