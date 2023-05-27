import cv2
camera = cv2.VideoCapture(0)
while True :

    ret , image_camera = camera.read()
    print(ret)
    cv2.imshow('Camera', image_camera)
    cv2.waitKey(1)

