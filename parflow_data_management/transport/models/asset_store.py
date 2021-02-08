from django.contrib.auth import get_user_model
from django.db import models

from parflow_data_management.scheduler.models.cluster import Cluster
from parflow_data_management.scheduler.models.input_file import InputFile
from parflow_data_management.scheduler.models.output_file import OutputFile

# Abstract mapping of a file to its location on a remote machine
class AssetStore(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="asset_stores"
    )
    cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE, related_name="asset_stores"
    )
    inputs = models.ManyToManyField(InputFile, blank=True)
    outputs = models.ManyToManyField(OutputFile, blank=True)

    # Ingest a remote directory consisting of input data
    def ingest(self, input_dir):
        pass