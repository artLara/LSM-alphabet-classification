from HandsDetectorMP import HandsDetector
from src.StaticSignClassifier import StaticSignClassifier
from src.SignClassifier import SignClassifier

class Controller():
    def __init__(self):
        self.__MAX_FRAMES = 5
        self.__handsDetector = HandsDetector()
        self.__staticSignClassifier = StaticSignClassifier()
        self.__signClassifier = SignClassifier()

    def run(self, frames):
        hands = []
        for frame in frames:
            hand  = self.__handsDetector.detect(frame)
            if hand != None:
                coordNorm = hand.getLandmarksNormalized()
                letter, sm_value = self.__staticSignClassifier.classify(coordNorm)
                hand.setLetter(letter)
                hand.setSMValue(sm_value)
                hands.append(hand)
            pass

        #Calling FinalClassifier
        best = ('', 0)
        for ind in range(len(hands)):
            hand = self.__signClassifier.classify(self.generateWindow(hands, ind))
            if hand.getSMValue() > best[1]:
                best = (hand.getLetter(), hand.getSMValue())

        return best[0]
    
    def generateWindow(self, hands, ind):
        start = ind
        end = max(len(hands), ind+self.__MAX_FRAMES)
        return hands[start:end]