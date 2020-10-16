from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from scheduler.models.conceptual_model import ConceptualModel

class ConceptualModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptualModel
        fields = ("id", "project")

class ConceptualModelViewSet(ModelViewSet):
    queryset = ConceptualModel.objects.all()

    serializer_class = ConceptualModelSerializer
