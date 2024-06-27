from KLetterDetector import KLetterDetector
from DoubleLetterDetector import DoubleLetterDetector
class SignClassifier():
    def __init__(self):
        self.__kLetterDetector = KLetterDetector()
        self.__doubleLetterDetector = DoubleLetterDetector()

    def classify(self, hands):
        letterHand = hands[0]
        for hand in hands:
            if self.__doubleLetterDetector.detect(hand):
                print('DOUBLE LETTER DETECTED!!!!!')
                letterHand.doubleLetter()
                break

            if self.__kLetterDetector.detect(hand):
                letterHand.setLetter('k')
                break

        return letterHand

            