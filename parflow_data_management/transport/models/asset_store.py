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

    # TODO: put this in a loop eventually? Keep one connection open,
    # add inputs and outputs in bulk?
    def register_file(self, file_t, file_id):
        file = file_t.objects.filter(pkey=file_id)[0]
        if file_t is InputFile:
            self.inputs.add(file)
        elif file_t is OutputFile:
            self.outputs.add(file)
        # TODO: error checking for unrecognized file_t

        self.save()
