from KLetterDetector import KLetterDetector
from DoubleLetterDetector import DoubleLetterDetector
class SignClassifier():
    def __init__(self):
        self.__kLetterDetector = KLetterDetector()
        self.__doubleLetterDetector = DoubleLetterDetector()

    def classify(self, hands, verbose=False):
        if verbose:
            print('Hands size:{}'.format(len(hands)))
            print('Checking:', end='')
            for hand in hands:
                print('({},{}) '.format(int(hand.getLandmarks()[21]),
                                    int(hand.getLandmarks()[0])), 
                                    end='')
            print(' wbb: {}'.format(hands[0].getWidthBoundingBox()))

        letterHand = hands[0]

        for hand in hands:
            if self.__kLetterDetector.detect(hand):
                letterHand.setLetter('k')
                return letterHand
            
        for hand in hands:
            if self.__doubleLetterDetector.detect(hand):
                letterHand.doubleLetter()
                return letterHand
        
        return letterHand