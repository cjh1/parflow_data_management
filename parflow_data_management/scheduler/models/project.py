from config.settings.base import AUTH_USER_MODEL
from django_extensions.db.models import TimeStampedModel
from django.db import models


class Project(TimeStampedModel, models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects")
    # TODO: more fields,
