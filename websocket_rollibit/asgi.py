
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_rollibit.settings')

import django

django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": URLRouter(routing.websocket_urlpatterns) }
)

