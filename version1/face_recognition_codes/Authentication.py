import cv2
import face_recognition
import pickle

file_read = open('faces_databse', 'rb')
faces_databse = pickle.load(file_read)

file_read = open('face_ids', 'rb')
face_ids = pickle.load(file_read)

image_path = 'test_img.png'

def Auth(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image,boxes)

    # for i,face in enumerate(face_encodings):
    #     box = boxes[i]
    results = []

    for box,face in zip(boxes,face_encodings):
        result = face_recognition.compare_faces(faces_databse, face)
        results.append(result)

    print(len(results))
    print(results)