from . import consumers
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r'ws/trivia/(?P<game_num>\w+)/$', consumers.TriviaConsumer.as_asgi()),
]