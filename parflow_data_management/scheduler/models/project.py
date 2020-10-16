from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.db import models


class Project(TimeStampedModel, models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="projects")
    # TODO: more fields,
