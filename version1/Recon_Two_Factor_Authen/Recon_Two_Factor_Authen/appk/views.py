from .forms import ImageForm
from django.http.response import StreamingHttpResponse
from appk.camera import VideoCamera

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
 
import os
import datetime

 
from django.http import HttpResponse



def index(request):
	return render(request, 'admin.html')


def vid(request):
	return render(request, 'vid.html')


def bien(request):
	return render(request, 'bien.html', {"droit": True})


def pro(request):
	return render(request, 'dash.html')


def acc(request):
	return render(request, 'acc.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_cam(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                              content_type='multipart/x-mixed-replace; boundary=frame')


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
                new_filename = f"image.jpg"
                with open(f'images/{new_filename}', 'wb+') as images:
                   for chunk in image_file.chunks():
                       images.write(chunk)

                return redirect('login')

                


                
                
        else:
            
            return render(request, 'reg.html', {'error': 'Password does not match!'})

       

    else:
         
        return render(request, 'reg.html' )
 

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('vid')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('acc')




def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        new_filename = f"image.jpg"
        with open(f'images/{new_filename}', 'wb+') as images:
            for chunk in image_file.chunks():
                images.write(chunk)
        
        return HttpResponse('File uploaded successfully.')
    
    return render(request, 'upload_image.html')



def success(request):
    return HttpResponse('Image Uploaded Successfully')
