# chat/routing.py
from django.urls import re_path
import video.consumer

websocket_urlpatterns = [
	re_path(r'video/(?P<v_name>\w+)/$', video.consumer.VideoConsumer.as_asgi())
]
