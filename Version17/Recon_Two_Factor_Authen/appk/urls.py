from django.urls import path, include


urlpatterns = [
    # path('', views.index, name='index'),
    path('video_cam', views.video_cam, name='video_cam'),
]
