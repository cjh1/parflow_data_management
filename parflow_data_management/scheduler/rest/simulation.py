from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from scheduler.models.simulation import Simulation

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = ("id", "project")

class SimulationViewSet(ModelViewSet):
    queryset = Simulation.objects.all()

    serializer_class = SimulationSerializer
