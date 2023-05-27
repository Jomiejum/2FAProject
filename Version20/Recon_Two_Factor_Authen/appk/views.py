# Sign up working
# Login from uploaded image working
from .forms import ImageForm
from django.http.response import StreamingHttpResponse
from appk.camera import VideoCamera,IPWebCam

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import numpy as np
import datetime
import os
import cv2
from face_rec.SIGNUP_add_person_to_database import *
from face_rec.Authentication import Auth

from django.http import HttpResponse
import time


def index(request):
    return render(request, 'admin.html')


def vid(request):
    return render(request, 'vid.html')


# def bien(request):
#     return render(request, 'bien.html', {"droit": True})

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')


def dash(request):
    return render(request, 'dash.html')


def acc(request):
    return render(request, 'acc.html')

def gen(camera,request):
    start = time.time()
    Verified = False
    if request.user.is_authenticated:
        # If the user is authenticated, get the username
        username = request.user.username

    while time.time() - start < 1000:
        frame = camera.get_frame()
        # print(camera.image.shape)
        # print(camera.identity)
        if camera.identity==username:
            Verified = True
        print('Verified')

        # if (time.time() - start > 9) and Verified :
        #     print('redirecting')
        #     redirect('video_cam')

        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_cam(request):


    camera = VideoCamera()
    camera.get_frame()

    return StreamingHttpResponse(gen(camera,request),
                                     content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)

            return redirect('video_cam')
            # return redirect('upload_image')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')





def reg(request):
    if request.method == "POST" and request.FILES['image']:

        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])

                return render(request, 'reg.html', {'error': 'Username is already taken!'}, )
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                auth.login(request, user)

                image_file = request.FILES['image']
                usrname = request.POST['username']
                print('usrname', usrname)
                new_filename = str(usrname) + ".jpg"
                image_data = np.fromstring(image_file.read(), np.uint8)
                image_opencv = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

                print(os.listdir(os.getcwd()))
                faces_databse, face_ids = database_cr()
                faces_databse, face_ids = addition(image_opencv, str(usrname), faces_databse, face_ids)
                print(face_ids)
                print(print('current path ', os.getcwd()))
                save_faces_database(faces_databse, face_ids)
                print(image_opencv.shape)

                with open(f'images/{new_filename}', 'wb+') as images:
                    for chunk in image_file.chunks():
                        images.write(chunk)

                return redirect('login')
        else:
            return render(request, 'reg.html', {'error': 'Password does not match!'})
    else:

        return render(request, 'reg.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')


def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']

        image_data_login = np.fromstring(image_file.read(), np.uint8)
        image_opencv_login = cv2.imdecode(image_data_login, cv2.IMREAD_COLOR)
        # cv2.imshow('image_opencv_login',image_opencv_login)
        # cv2.waitKey(0)
        # image_opencv_login, identity = Auth(image_opencv_login)
        # image_opencv_login = cv2.cvtColor(image_opencv_login,cv2.COLOR_BGR2RGB)

        image_opencv_login, identity = Auth(image_opencv_login)
        print('identity = ', identity)
        cv2.imshow('image_opencv_login', image_opencv_login)
        cv2.waitKey(0)
        new_filename = f"image.jpg"
        with open(f'images/{new_filename}', 'wb+') as images:
            for chunk in image_file.chunks():
                images.write(chunk)

        return HttpResponse('File uploaded successfully.')

    return render(request, 'upload_image.html')


def success(request):
    return HttpResponse('Image Uploaded Successfully')
