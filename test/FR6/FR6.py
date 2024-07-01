import sys
sys.path.append('../../')
sys.path.insert(0, '/home/lara/Documents/lsm/LettersPapper/LSM-alphabet-classification/src')
from src.FileLoader import FileLoader
from src.Hand import Hand
from src.HandsDetectorMP import HandsDetector
from src.StaticSignClassifier import StaticSignClassifier
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
import numpy as np

class FR6():
    def __init__(self):
        self.__path = '../media/'
        self.__handsDetector = HandsDetector()
        self.__classifier = StaticSignClassifier()

    def loadTestingDataset(self):
        infile = open(self.__path+'landmarks','rb')
        X = pickle.load(infile)
        infile.close()
        infile = open(self.__path+'targets','rb')
        y = pickle.load(infile)
        infile.close()
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        x_test=np.asarray(x_test, dtype=np.float32)
        y_train=np.asarray(y_train)
        y_test=np.asarray(y_test)
        onehot_encoder = OneHotEncoder(sparse_output=False)
        y_train = y_train.reshape(len(y_train), 1)
        y_train_onehot = onehot_encoder.fit_transform(y_train)

        y_test = y_test.reshape(len(y_test), 1)
        y_test_onehot = onehot_encoder.fit_transform(y_test)

        return x_test,  y_test

    def run(self):
        x_test,y_test = self.loadTestingDataset()
        print('X test shape:{}'.format(x_test.shape))
        print('y test shape:{}'.format(y_test.shape))
        m = np.zeros((len(self.__classifier.getDictOneHot()),len(self.__classifier.getDictOneHot())))
        y_true = []
        y_pred = []
        for index,_ in enumerate(x_test):
            # try:
            y_p, _ = self.__classifier.classify(x_test[index:index+1])
            y_pred.append(y_p)
            y_true.append(y_test[index][0])
            # print('y_pred: {} y_true:{}'.format(y_p, y_test[index][0]))
            y_true_index = [k for k, v in self.__classifier.getDictOneHot().items() if v == y_test[index][0]][0]
            y_pred_index = [k for k, v in self.__classifier.getDictOneHot().items() if v == y_p][0]
            # print(keys)
            m[y_pred_index][y_true_index] += 1

        print(m)
        score = f1_score(y_true, y_pred, average="macro")
        print("F1-Score: ", score)
        score = precision_score(y_true, y_pred, average="macro")
        print("Precision-Score: ", score)
        score = recall_score(y_true, y_pred, average="macro")
        print("Recall-Score: ", score)
        score = accuracy_score(y_true, y_pred)
        print("Accuracy-Score: ", score)

        # print('Total frames:{}'.format(len(frames)))
        # print('Detected:{}'.format(detected))
        # print('Not detected:{}'.format(notDetected))
        # print('Len:{}'.format(len(letters)))
        # print('Info:{}'.format(letters))


fr = FR5()
print('#######Metrics and confussion matrix of static signs#############')
fr.run()