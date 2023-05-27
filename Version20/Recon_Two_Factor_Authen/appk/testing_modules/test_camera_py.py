import cv2
from camera2 import VideoCamera


# while True :
verif = False
cam = VideoCamera(verif)
cam.get_frame()
print(cam.verif)

#img = vid_camera.get_frame