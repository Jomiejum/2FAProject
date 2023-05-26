from django.urls import path, include
from narimen import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('video_cam', views.video_cam, name='video_cam'),
]
