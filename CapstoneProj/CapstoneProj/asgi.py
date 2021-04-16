"""
ASGI config for CapstoneProj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
from trivia import consumers


import django
from channels.http import AsgiHandler
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from trivia.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trivia.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # "channels": ChannelNameRouter({
  #   "update-question": consumers.question.as_asgi(),

  # }),
  'websocket': AuthMiddlewareStack(URLRouter(
      websocket_urlpatterns
    )
  )
  ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})