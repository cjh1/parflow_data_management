from django.contrib.auth import get_user_model
from django.db import models

from parflow_data_management.scheduler.models import cluster, input_file, output_file

# Abstract mapping of a file to its location on a remote machine
class AssetStore(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="asset_stores"
    )
    cluster = models.ForeignKey(
        cluster.Cluster, on_delete=models.CASCADE, related_name="asset_stores"
    )
    inputs = models.ManyToManyField(input_file.InputFile, blank=True)
    outputs = models.ManyToManyField(output_file.OutputFile, blank=True)

    def register_files(self):
        pass
