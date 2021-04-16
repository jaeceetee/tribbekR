from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import trivia

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack({
        URLRouter(
            trivia.routing.websocket_urlpatterns
        )
    })
})



# from channels.routing import ProtocolTypeRouter, URLRouter
# from trivia.routing import websockets
# from trivia.middlewares import TokenAuthMiddlewareStack
# application = ProtocolTypeRouter({
#     "websocket": TokenAuthMiddlewareStack(websockets),
# })