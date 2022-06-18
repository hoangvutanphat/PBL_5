from webcam.views import index, video_feed
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('video_feed/', video_feed, name="video-feed")
]
