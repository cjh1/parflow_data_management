from django.urls import include, path
from rest_framework import routers
from .rest import project, simulation

router = routers.DefaultRouter()
router.register(r'projects', project.ProjectViewSet)
router.register(r'simulations', simulation.SimulationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]