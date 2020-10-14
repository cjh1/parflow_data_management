from django.urls import include, path
from rest_framework import routers
from .rest import project

router = routers.DefaultRouter()
router.register(r'projects', project.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]