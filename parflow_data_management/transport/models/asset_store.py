from django.contrib.auth import get_user_model
from django.db import models

from ..scheduler.models.cluster import Cluster

# Abstract mapping of a file to its location on a remote machine
class AssetStore:
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="asset_stores"
    )
    cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="asset_stores"
    )


    def register_files(self):
        pass