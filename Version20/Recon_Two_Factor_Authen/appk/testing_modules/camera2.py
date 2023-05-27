import cv2

class VideoCamera(object):
    def __init__(self,verif):
        print('__init__')
        self.video = cv2.VideoCapture(0)
        self.verif = verif

    def get_frame(self):
        print('get_frame')
        # while True :
        # self.verif = True
        self.verif = True
        success, self.image = self.video.read()
        # image, identity = self.recognize(image)
        # print('self.image',self.image.shape)
        # cv2.imshow('image', self.image)
        # cv2.waitKey(1)

