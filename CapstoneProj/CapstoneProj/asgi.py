"""
ASGI config for CapstoneProj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'CapstoneProj.CapstoneProj.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CapstonProj.CapstoneProj.settings")
import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from django.conf import settings
settings.configure(DEBUG=True)
django.setup()


from django.conf.urls import url
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()
from channels.http import AsgiHandler
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from CapstoneProj.trivia.routing import websocket_urlpatterns


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