from config.settings.base import AUTH_USER_MODEL
from django_extensions.db.models import TimeStampedModel
from django.db import models

from .project import Project


class Simulation(TimeStampedModel, models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="simulations"
    )
