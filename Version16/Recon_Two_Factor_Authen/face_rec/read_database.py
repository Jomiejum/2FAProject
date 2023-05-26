import cv2
import face_recognition
import pickle


file_read = open('face_ids', 'rb')
face_ids = pickle.load(file_read)
print(face_ids)
