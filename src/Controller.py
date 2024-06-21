from HandsDetectorMP import HandsDetector
from SignClassifier import SignClassifier
class Controller():
    def __init__(self):
        self.__MAX_FRAMES = 5
        self.__handsDetector = HandsDetector()
        self.__classifier = SignClassifier()

    def run(self, frames):
        letters = []
        for frame in frames:
            hand  = self.__handsDetector.detect(frame)
            if hand != None:
                coordNorm = hand.getLandmarksNormalized()
                letter, sm_value = self.__classifier(coordNorm)
                letters.append((letter, sm_value))
            pass

        #Calling FinalClassifier
        print(letters)