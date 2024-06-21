import filetype
import cv2

class FileLoader():
    def __init__(self):
        pass

    def load(self, fileName, path=''):
        if filetype.is_image(path+fileName):
            return self.loadImage(fileName, path)

        elif filetype.is_video(path+fileName):
            return self.loadVideo(fileName, path)

        else:
            print('Error with the file', fileName)
        pass

    def loadImage(self, fileName, path):
        img = cv2.imread(path+fileName, cv2.IMREAD_COLOR)
        # img = cv2.flip(img, 1) #Change it in case of left hand
        return self.padding(img)

    def padding(self, image):
        return [image]

    def loadVideo(self, fileName, path):
        frames = []
        vidObj = cv2.VideoCapture(path+fileName) 
        success, img = vidObj.read() 
        while success: 
            img = cv2.flip(img, 1) #Change it in case of left hand
            frames.append(img)
            success, img = vidObj.read() 

        return frames