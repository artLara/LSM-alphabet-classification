from KLetterDetector import KLetterDetector
from DoubleLetterDetector import DoubleLetterDetector
class SignClassifier():
    def __init__(self):
        self.__kLetterDetector = KLetterDetector()
        self.__doubleLetterDetector = DoubleLetterDetector()

    def classify(self, hands):
        # print(len(hands))
        # print('Checking:', end='')
        letterHand = hands[0]
        for hand in hands:
            if self.__doubleLetterDetector.detect(hand):
                letterHand.doubleLetter()
                break


            # if self.__kLetterDetector.detect(hand):
            #     letterHand.setLetter('k')
            #     break
        
        # print(' wbb: {}'.format(hands[0].getWidthBoundingBox()))
        return letterHand

            