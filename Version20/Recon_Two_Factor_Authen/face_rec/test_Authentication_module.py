from Authentication import Auth
import cv2
import pickle

file_read = open('faces_databse', 'rb')
faces_database = pickle.load(file_read)

file_read = open('face_ids', 'rb')
face_ids = pickle.load(file_read)


image = cv2.imread('ch.jpeg')
output_image,identity = Auth(image)
print(identity)
cv2.imshow('output_image',output_image)
cv2.waitKey(0)