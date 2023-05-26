import cv2


class VideoCamera(object):
    def __init__(self):
        self.image = cv2.imread('./images/image.jpg')

    def get_frame(self):

        ret, jpeg = cv2.imencode('.jpg', self.image)

        return jpeg.tobytes()

# image = cv2.imread('image.png')
# print(image.shape)
# cv2.imshow('aa',image)
# cv2.waitKey(0)
