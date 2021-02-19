from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from parflow_data_management.scheduler.models.folder import Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()

    serializer_class = FolderSerializer
