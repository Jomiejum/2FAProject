import cv2
import face_recognition
import pickle

# file_read = open('faces_databse', 'rb')
# faces_databse = pickle.load(file_read)
#
# file_read = open('face_ids', 'rb')
# face_ids = pickle.load(file_read)

def load_faces():
    file_read = open('faces_databse', 'rb')
    faces_databse = pickle.load(file_read)

    file_read = open('face_ids', 'rb')
    face_ids = pickle.load(file_read)

    return faces_databse,face_ids

def resize_image(image, new_width):
    h, w , _ = image.shape
    new_height = int(h * new_width / w)
    new_size = (new_width, new_height)

    image = cv2.resize(image, new_size)

    return image



def draw_rec(image,boxes):

    for (top, right, bottom, left) in boxes :
        start_pt = (left, top)
        end_pt = (right, bottom)
        color = (255, 0, 0)
        thickness = 2
        image = cv2.rectangle(image, start_pt, end_pt, color, thickness)

    return image


def visulize_identity(image,identity,box):

    (top, right, bottom, left) = box
    start_x = int(((right + left) / 2)-50)
    start_y = int(top - 10)
    start_pt =  (start_x,start_y)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    image = cv2.putText(image, str(identity),start_pt , font,
                        fontScale, color, thickness, cv2.LINE_AA)
    return image


def Auth(prediction_image):
    faces_database,face_ids = load_faces()
    prediction_image = cv2.cvtColor(prediction_image, cv2.COLOR_BGR2RGB)

    new_width = 1000
    prediction_image = resize_image(prediction_image, new_width)

    boxes = face_recognition.face_locations(prediction_image)
    prediction_faces = face_recognition.face_encodings(prediction_image)

    prediction_image = draw_rec(prediction_image, boxes)


    for i,face in enumerate(faces_database):

        identity = 'Unknown'
        results = face_recognition.compare_faces(prediction_faces, face)

        if True in results:
            print(results)
            idx = results.index(True)
            print(idx)
            print(i)
            identity = face_ids[i]
            box = boxes[results.index(True)]
            visulize_identity(prediction_image, identity, box)

    return prediction_image,identity