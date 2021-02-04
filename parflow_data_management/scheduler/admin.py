from django.contrib import admin
from .models import (
    cluster,
    conceptual_model,
    input_file,
    mesh,
    metadata,
    output_file,
    project,
    simulation,
    workflow,
)

admin.site.register(cluster.Cluster)
admin.site.register(conceptual_model.ConceptualModel)
admin.site.register(input_file.InputFile)
admin.site.register(mesh.Mesh)
admin.site.register(metadata.Metadata)
admin.site.register(output_file.OutputFile)
admin.site.register(project.Project)
admin.site.register(simulation.Simulation)
admin.site.register(workflow.Workflow)
