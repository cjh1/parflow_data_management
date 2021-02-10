from django.db import models
from django_extensions.db.models import TimeStampedModel

from .project_asset import ProjectAsset


class Folder(TimeStampedModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="folders",
    )
