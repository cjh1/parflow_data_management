from django.db import models
from .project import Project


# Abstract class encapsulating common data shared by
# components of a project
class ProjectAsset(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(class)ss")

    class Meta:
        abstract = True

def check_project_asset_perm(user, perm, proj_asset):
    # First get the related project
    proj = proj_asset.project

    # Check if the user has the corresponding permission
    # on the parent project
    return user.has_perm(perm, proj)