from rest_framework import serializers
from parflow_data_management.scheduler.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id, owner")

