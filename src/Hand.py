import numpy as np

class Hand():
    def __init__(self):
        self.__imgWidth = None
        self.__imgHeight = None
        self.__landmarksNormalized = None
        self.__landmarks = None
        self.__boundingBox = None
        self.__letter = ""
        self.__confidense = None
        self.__smValue = None

    def getImgWidth(self):
        return self.__imgWidth
    def getImgHeight(self):
        return self.__imgHeight
    def getLandmarksNormalized(self):
        return self.__landmarksNormalized
    def getLandmarks(self):
        return self.__landmarks
    def getBoundingBox(self):
        return self.__boundingBox
    def getLetter(self):
        return self.__letter
    def getConfidense(self):
        return self.__confidense
    def getSMValue(self):
        return self.__smValue

    def getWidthBoundingBox(self):
        return self.__boundingBox[3]-self.__boundingBox[1]

    def getHeightBoundingBox(self):
        if self.__boundingBox == None:
            return -1
        return self.__boundingBox[2]-self.__boundingBox[0]
    
    def getAttributes(self):
        attributes = {}
        attributes['imgWidth']= self.__imgWidth
        attributes['imgHeight'] = self.__imgHeight
        attributes['landmarksNormalized'] = self.__landmarksNormalized.tolist()
        attributes['landmarks'] = self.__landmarks.tolist()
        attributes['boundingBox'] = self.__boundingBox
        attributes['letter'] = self.__letter 
        attributes['confidense'] = self.__confidense
        return attributes
    
    def setAttributes(self, attributes):
        self.__imgWidth = attributes['imgWidth']
        self.__imgHeight = attributes['imgHeight']
        self.__landmarksNormalized = np.asarray(attributes['landmarksNormalized'])
        self.__landmarks = np.asarray(attributes['landmarks'])
        self.__boundingBox = attributes['boundingBox']
        self.__letter = attributes['letter']
        self.__confidense = attributes['confidense']

    ####### SETTERS
    def setImgWidth(self, tmp):
        self.__imgWidth = tmp
    def setImgHeight(self, tmp):
        self.__imgHeight = tmp
    def setLandMarksNormalized(self, tmp):
        self.__landmarksNormalized = tmp
    def setLandMarks(self, tmp):
        self.__landmarks = tmp
    def setBoundingBox(self, tmp):
        self.__boundingBox = tmp
    def setLetter(self, tmp):
        self.__letter = tmp
    def setConfidense(self, tmp):
        self.__confidense = tmp
    def setSMValue(self, tmp):
        self.__smValue = tmp

    def doubleLetter(self):
        self.__letter += self.__letter

