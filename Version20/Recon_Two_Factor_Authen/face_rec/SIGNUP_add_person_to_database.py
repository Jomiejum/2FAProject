import cv2
import face_recognition
import pickle
import os
from random import randint

def database_cr():
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    print('current path ',os.getcwd())
    faces_databse_path = 'faces_databse'
    print(faces_databse_path)
    database_exist = os.path.exists(faces_databse_path)

    # print(database_exist)
    if database_exist :
        file_read = open('faces_databse', 'rb')
        faces_databse = pickle.load(file_read)

        file_read = open('face_ids', 'rb')
        face_ids = pickle.load(file_read)

    else :
        faces_databse = []
        face_ids = []

    return faces_databse,face_ids

def generate_id(face_ids):
    while True:
        id = randint(1000000, 9999999)
        if id not in face_ids:
            break
    return id

# faces_databse,face_ids = database_cr()


def addition(image,user_name,faces_databse,face_ids):

    # image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_encoding = face_recognition.face_encodings(image)[0]
    faces_databse.append(face_encoding)
    face_ids.append(user_name)

    return faces_databse,face_ids

# faces_databse,face_ids  = addition(image,faces_databse,face_ids)
def save_faces_database(faces_databse,face_ids):

    file_saving = open('faces_databse', 'wb')
    pickle.dump(faces_databse,file_saving)

    file_saving = open('face_ids', 'wb')
    pickle.dump(face_ids,file_saving)

# print(face_ids)