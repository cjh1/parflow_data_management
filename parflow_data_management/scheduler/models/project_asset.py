from django.db import models
from .project import Project


# Abstract class encapsulating common data shared by
# components of a project
class ProjectAsset(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        abstract = True
