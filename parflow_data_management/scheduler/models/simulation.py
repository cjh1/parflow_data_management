from config.settings.base import AUTH_USER_MODEL
from django_extensions.db.models import TimeStampedModel
from django.db import models

from .project import Project
from .project_asset import ProjectAsset

class Simulation(TimeStampedModel, ProjectAsset):
    pass
