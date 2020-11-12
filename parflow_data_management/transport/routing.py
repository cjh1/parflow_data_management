from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import KeyConsumer
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from django.urls import re_path

channel_routing = [
    re_path(r"ws/keygen/$", KeyConsumer.as_asgi()),
]