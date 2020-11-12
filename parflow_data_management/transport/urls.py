from django.urls import path

from . import views

urlpatterns = [
    path("key-generation-test/", views.keygen_view),
    path("keypairs/", views.start_keygen),
]