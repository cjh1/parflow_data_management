from django_extensions.db.models import TimeStampedModel

from .project_asset import ProjectAsset

class Metadata(TimeStampedModel, ProjectAsset):
    pass
