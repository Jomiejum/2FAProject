 
from django.contrib import admin
from django.urls import path, include
from appk import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    # path('vidCam/', views.vid,name='vid'),
    path('dash/', views.dash, name='dash'),
    path('video_cam', views.video_cam, name='video_cam'),

    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout, name='logout'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('success/', views.success, name='success'),
]   