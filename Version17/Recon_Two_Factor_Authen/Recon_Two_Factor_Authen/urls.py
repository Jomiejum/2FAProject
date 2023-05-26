 
from django.contrib import admin
from django.urls import path, include
from appk import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('dash/', views.index, name='dash'),
    # path('vidCam/', views.vid,name='vid'),
    # path('home/', views.home, name='home'),
    path('pro/', views.pro, name='pro'),
    path('video_cam', views.video_cam, name='video_cam'),
    path('login/', views.login, name='login'),
    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout, name='logout'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('success/', views.success, name='success'),
]