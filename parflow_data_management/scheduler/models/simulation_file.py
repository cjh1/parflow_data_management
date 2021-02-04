from django.db import models
from django_extensions.db.models import TimeStampedModel

from .project_asset import ProjectAsset


class SimulationFile(TimeStampedModel, ProjectAsset):
    path = models.FilePathField("/")
